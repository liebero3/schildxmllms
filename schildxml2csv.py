import argparse

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import xml.etree.ElementTree as ET

import csv


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # if you use base it is obligatory

    lehrerid = Column(String, primary_key=True)  # obligatory
    name = Column(String)
    given = Column(String)
    institutionrole = Column(String)
    email = Column(String)

    def __init__(self, lehrerid, name, given, institutionrole, email):
        self.lehrerid = lehrerid
        self.name = name
        self.given = given
        self.institutionrole = institutionrole
        self.email = email

    def __repr__(self):  # optional
        return f'User {self.name}'


class Group(Base):
    __tablename__ = 'groups'

    groupid = Column(String, primary_key=True)
    name = Column(String)
    parent = Column(String)

    def __init__(self, groupid, name, parent):
        self.groupid = groupid
        self.name = name
        self.parent = parent

    def __repr__(self):  # optional
        return f'Group {self.name}'


class Membership(Base):
    __tablename__ = 'memberships'

    membershipid = Column(Integer, primary_key=True)
    groupid = Column(String)
    nameid = Column(String)

    def __init__(self, membershipid, groupid, nameid):
        self.membershipid = membershipid
        self.groupid = groupid
        self.nameid = nameid

    def __repr__(self):  # optional
        return f'Group {self.groupid}'


def readusers():
    for elem in root.findall(
            ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}person"):
        for child in elem.findall(
                ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}id"):
            lehrerid = child.text
        for child in elem.findall(
                ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}family"):
            name = child.text
        for child in elem.findall(
                ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}given"):
            given = child.text
        for child in elem.findall(".//{http://www.metaventis.com/ns/cockpit/sync/1.0}institutionrole"):
            institutionrole = child.get('institutionroletype')
        email = ""
        for child in elem.findall(
                ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}email"):
            email = child.text
        user = User(lehrerid, name, given, institutionrole, email)
        session.add(user)

    session.commit()


def readgroups():
    parent = ''
    for elem in root.findall(
            ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}group"):
        for child in elem.findall("{http://www.metaventis.com/ns/cockpit/sync/1.0}sourcedid/{http://www.metaventis.com/ns/cockpit/sync/1.0}id"):
            groupid = child.text
        # use short or long as course info
        for child in elem.findall("{http://www.metaventis.com/ns/cockpit/sync/1.0}description/{http://www.metaventis.com/ns/cockpit/sync/1.0}short"):
            name = child.text
        for child in elem.findall("{http://www.metaventis.com/ns/cockpit/sync/1.0}relationship/{http://www.metaventis.com/ns/cockpit/sync/1.0}sourcedid/{http://www.metaventis.com/ns/cockpit/sync/1.0}id"):
            parent = child.text

        group = Group(groupid, name, parent)
        session.add(group)

    session.commit()


def readmemberships():
    i = 0

    for elem in root.findall(
            ".//{http://www.metaventis.com/ns/cockpit/sync/1.0}membership"):

        for child in elem.findall("{http://www.metaventis.com/ns/cockpit/sync/1.0}sourcedid/{http://www.metaventis.com/ns/cockpit/sync/1.0}id"):
            groupid = child.text
            # print(child.text)
        for child in elem.findall("{http://www.metaventis.com/ns/cockpit/sync/1.0}member/{http://www.metaventis.com/ns/cockpit/sync/1.0}sourcedid/{http://www.metaventis.com/ns/cockpit/sync/1.0}id"):
            nameid = child.text
            # print(child.text)
            # print(i)

        membership = Membership(i, groupid, nameid)
        session.add(membership)

        i += 1

    session.commit()


def readfile():
    readusers()
    readgroups()
    readmemberships()


def returnCoursesOfStudent(studentid):
    courseslist = []
    for group, in session.query(
            Membership.groupid).filter(
            Membership.nameid == studentid):
        groupname, = session.query(Group.name).filter(Group.groupid == group)
        courseslist.append(groupname[0])
    courses = "|".join(courseslist)
    return courses


def returnLastname(studentid):
    last, = session.query(User.name).filter(User.lehrerid == studentid)
    return(last[0])


def returnGivenname(studentid):
    given, = session.query(User.given).filter(User.lehrerid == studentid)
    return(given[0])


def returnInstitutionrole(studentid):
    institutionrole, = session.query(
        User.institutionrole).filter(
        User.lehrerid == studentid)
    return(institutionrole[0])


def returnEmail(studentid):
    email, = session.query(
        User.email).filter(
        User.lehrerid == studentid)
    return(email[0])


def returnPassword(studentid):
    return(studentid)


def returnUsername(studentid):
    last, = session.query(User.name).filter(User.lehrerid == studentid)
    given, = session.query(User.given).filter(User.lehrerid == studentid)
    username = given[0].split(" ")[0] + "." + last[0]

    return username.lower().replace(
        "ü", "ue").replace(
        "ä", "ae").replace(
        "ö", "oe").replace(
        "á", "a").replace(
        "à", "a").replace(
        "é", "e").replace(
        "è", "e").replace(
        "ó", "o").replace(
        "ò", "o").replace(
        "â", "a").replace(
        "ê", "e").replace(
        "û", "u").replace(
        "ë", "e").replace(
        " ", "").replace(
        "ß", "ss").replace(
        "ï", "i").replace(
        "ÿ", "y").replace(
        "ã", "a").replace(
        "å", "a").replace(
        "æ", "ae").replace(
        "ç", "c").replace(
        "ì", "i").replace(
        "í", "i").replace(
        "î", "i").replace(
        "ð", "d").replace(
        "ñ", "n").replace(
        "ô", "o").replace(
        "õ", "o").replace(
        "ø", "oe").replace(
        "œ", "oe").replace(
        "ù", "u").replace(
        "ú", "u").replace(
        "ý", "y").replace(
        "š", "s").replace(
        "č", "c")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input_xml_file", required=True,
                    help="name des xmlfiles angeben")
    ap.add_argument("-o", "--output_csv_file", required=True,
                    help="name der csv angeben")
    args = vars(ap.parse_args())
    print(args['input_xml_file'])
    tree = ET.parse(args['input_xml_file'])
    root = tree.getroot()
    engine = create_engine(
        f"sqlite:///{args['input_xml_file'].strip('.xml')}.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    readfile()
    # returnCoursesOfStudent('ID-123456-3417')
    with open(args['output_csv_file'], 'w', encoding="utf-8", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            ["idnumber"] + ["username"] + ["firstname"] + ["lastname"] +
            ["profile_field_Klasse"] + ["password"] + ["email"] +
            ["profile_field_Lehrer_in"])
        for userid, in session.query(User.lehrerid):
            spamwriter.writerow(
                [f"{userid}"] + [returnUsername(userid)] +
                [returnGivenname(userid)] + [returnLastname(userid)] +
                [returnCoursesOfStudent(userid)] + [returnPassword(userid)] +
                [(f"{userid}@example.com", returnEmail(userid))[returnEmail(userid) != ""]] +
                [("0", "1")[returnInstitutionrole(userid) == "Faculty"]])
