import copy
import re
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMessageBox


def converted_rep(rep):
    for x in range(len(rep)):
        if rep[x] == 'No detail available':
            rep[x] = 0
        else:
            rep[x] = int(rep[x].replace(',', ''))
    return rep

def dataa(data, at, tableWidget,af):
    data_copy = data()
    data_copy.title = copy.copy(data.title)
    data_copy.answers = copy.copy(data.answers)
    data_copy.views = copy.copy(data.views)
    data_copy.votes = copy.copy(data.votes)
    data_copy.users = copy.copy(data.users)
    data_copy.reputation = copy.copy(data.reputation)
    data_copy.time_stamp = copy.copy(data.time_stamp)
    data_copy.summary = copy.copy(data.summary)
    if af == 'Title':
        search1(data_copy.title, at, tableWidget,data)
    if af == 'No. of answer':
        try:
            at = int(at)
            search2(data_copy.answers, at, tableWidget,data)
        except ValueError:
            # Handle the case where 'at' is not a valid integer
            QMessageBox.information(None, "Invalid Input","Please enter a valid integer for searching 'No. of answer'.")
    if af == 'No. of views':
        try:
            at = int(at)
            search2(data_copy.views, at, tableWidget,data)
        except ValueError:
            # Handle the case where 'at' is not a valid integer
            QMessageBox.information(None, "Invalid Input","Please enter a valid integer for searching 'No. of views'.")
    if af == 'No. of votes':
        try:
            at = int(at)
            search2(data_copy.votes, at, tableWidget,data)
        except ValueError:
            # Handle the case where 'at' is not a valid integer
            QMessageBox.information(None, "Invalid Input","Please enter a valid integer for searching 'No. of votes'.")
    if af == 'Tags':
        search1(data_copy.users, at, tableWidget,data)
    if af == 'Reputation of User':
        try:
            rep = converted_rep(data_copy.reputation)
            at = int(at)
            search2(rep, at, tableWidget,data)
        except ValueError:
            # Handle the case where 'at' is not a valid integer
            QMessageBox.information(None, "Invalid Input","Please enter a valid integer for searching 'Reputation of User'.")
    if af == 'Time Stamp':
        try:
            print(data_copy.time_stamp)
            at = int(at)
            search2(data_copy.time_stamp, at, tableWidget,data)
        except ValueError:
            # Handle the case where 'at' is not a valid integer
            QMessageBox.information(None, "Invalid Input","Please enter a valid integer for searching 'Time Stamp'.")
    if af == 'Summary':
        search1(data_copy.summary, at, tableWidget,data)


def columnreset(tableWidget):
    tableWidget.setRowCount(0) # Clear table
    tableWidget.setColumnCount(8)  # Display (7 columns)

    header_labels = ['Title', 'No. of answer', 'No. of views', 'No. of votes', 'Tags', 'Reputation of User', 'Time Stamp', 'Summary']
    tableWidget.setHorizontalHeaderLabels(header_labels)



# for start as


def search_start_as(data, search_word, tableWidget, af):
    columnreset(tableWidget)
    matching_rows = []
    if af == 'Title':
        for index, title in enumerate(data.title):
            # Extract the first word or letter of the data and compare it with the search word
            first_word = title.split()[0][0].lower()
            if first_word == search_word.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)
    if af == 'Tags':
        for index, title in enumerate(data.users):
            # Extract the first word or letter of the data and compare it with the search word
            first_word = title.split()[0][0].lower()
            if first_word == search_word.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)
    if af == 'Summary':
        for index, title in enumerate(data.summary):
            # Extract the first word or letter of the data and compare it with the search word
            first_word = title.split()[0][0].lower()
            if first_word == search_word.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)



    tableWidget.setRowCount(len(matching_rows))
    for row, matching_row in enumerate(matching_rows):
        for col, cell_data in enumerate(matching_row):
            item = QTableWidgetItem(cell_data)
            tableWidget.setItem(row, col, item)

    if not matching_rows:
        QMessageBox.information(None, "Search Result", f"No matching data found for words starting with '{search_word}' in the selected attribute.")


# simple search

def search1(data, search_word, tableWidget, classa):
    columnreset(tableWidget)
    matching_rows = []

    for index, title in enumerate(data):
        if search_word.lower() in title.lower():
            matching_row = [
                classa.title[index],
                str(classa.answers[index]),
                str(classa.views[index]),
                str(classa.votes[index]),
                classa.users[index],
                str(classa.reputation[index]),
                str(classa.time_stamp[index]),
                classa.summary[index]
            ]
            matching_rows.append(matching_row)

    # Sort matching_rows based on the 'title' column (you can change the column to sort by)
    matching_rows.sort(key=lambda x: x[0].lower())  # Sort based on the 'title' (case-insensitive)

    tableWidget.setRowCount(len(matching_rows))
    for row, matching_row in enumerate(matching_rows):
        for col, cell_data in enumerate(matching_row):
            item = QTableWidgetItem(cell_data)
            tableWidget.setItem(row, col, item)

    if not matching_rows:
        QMessageBox.information(None, "Search Result", f"No matching data found for '{search_word}' in the selected attribute.")


# for end as

def search_end_as(data, search_word, tableWidget, af):
    columnreset(tableWidget)
    matching_rows = []
    if af == 'Title':
        for index, title in enumerate(data.title):
            # Extract the last letter or word of the data and compare it with the search word
            last_word = title.split()[-1].lower()
            if last_word == search_word.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)
    if af == 'Tags':
        for index, title in enumerate(data.users):
            # Extract the last letter or word of the data and compare it with the search word
            last_word = title.split()[-1].lower()
            if last_word == search_word.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)
    if af == 'Summary':
        for index, title in enumerate(data.summary):
            # Extract the last letter or word of the data and compare it with the search word
            last_word = title.split()[-1].lower()
            if last_word == search_word.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)



    tableWidget.setRowCount(len(matching_rows))
    for row, matching_row in enumerate(matching_rows):
        for col, cell_data in enumerate(matching_row):
            item = QTableWidgetItem(cell_data)
            tableWidget.setItem(row, col, item)

    if not matching_rows:
        QMessageBox.information(None, "Search Result", f"No matching data found for words ending with '{search_word}' in the selected attribute.")


# contains

def search_contain(data, search_word, tableWidget, af):
    columnreset(tableWidget)
    matching_rows = []
    if af == 'Title':
        for index, title in enumerate(data.title):
            if search_word.lower() in title.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)
    if af == 'Tags':
        for index, title in enumerate(data.users):
            if search_word.lower() in title.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)
    if af == 'Summary':
        for index, title in enumerate(data.summary):
            if search_word.lower() in title.lower():
                matching_row = [
                    data.title[index],
                    str(data.answers[index]),
                    str(data.views[index]),
                    str(data.votes[index]),
                    data.users[index],
                    str(data.reputation[index]),
                    str(data.time_stamp[index]),
                    data.summary[index]
                ]
                matching_rows.append(matching_row)

    tableWidget.setRowCount(len(matching_rows))
    for row, matching_row in enumerate(matching_rows):
        for col, cell_data in enumerate(matching_row):
            item = QTableWidgetItem(cell_data)
            tableWidget.setItem(row, col, item)

    if not matching_rows:
        QMessageBox.information(None, "Search Result", f"No matching data found for '{search_word}' in the selected attribute.")


def search2(data, search_word, tableWidget,classa):

    columnreset(tableWidget)
    matching_rows = []

    try:
        search_int = int(search_word)  # Try to convert search_word to an integer
        for index, answer_count in enumerate(data):
            if search_int == answer_count:
                matching_row = [
                classa.title[index],
                str(classa.answers[index]),
                str(classa.views[index]),
                str(classa.votes[index]),
                classa.users[index],
                str(classa.reputation[index]),
                str(classa.time_stamp[index]),
                classa.summary[index]
                ]
                matching_rows.append(matching_row)
    except ValueError:
        # Handle the case where search_word is not an integer
        pass

    tableWidget.setRowCount(len(matching_rows))
    for row, matching_row in enumerate(matching_rows):
        for col, cell_data in enumerate(matching_row):
            item = QTableWidgetItem(cell_data)
            tableWidget.setItem(row, col, item)

    if not matching_rows:
        QMessageBox.information(None, "Search Result", f"No matching data found for '{search_word}' in the selected attribute.")



