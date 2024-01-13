import sys
from ui_code import Ui_MainWindow  # Import the generated UI code
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
import pandas as pd
import sorting
import copy
import Web_Scraping
import des_sorting
from PyQt5.QtCore import QThread, pyqtSignal


class data:
    def __init__(self):
        self.title = []
        self.answers = []
        self.views = []
        self.votes = []
        self.reputation = []
        self.time_stamp = []
        self.summary = []
        self.users = []


class WebScraping_thread(QThread):
    finished = pyqtSignal()
    stop_requested = False

    def run(self):
        self.stop_requested = False
        start = Web_Scraping.get_start_index()
        for x in range(start, 32185):
            if self.stop_requested:
                break
            Web_Scraping.web_scraping(x)
        self.finished.emit()

    def stop(self):
        print(f" stop called have been")
        self.stop_requested = True


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frameSearch.hide()
        self.ui.frameSort.hide()
        self.ui.frameScrap.hide()
        self.ui.tableWidget.hide()
        # Connect the button click event to the slot (function)
        self.ui.Sorting.clicked.connect(self.toggle_frame)
        self.ui.Searching.clicked.connect(self.toggle_frame1)
        self.ui.Scraping.clicked.connect(self.toggle_frame2)
        self.datas = self.loaddata() # load data into list
        self.loadtable(self.datas)  # load data into table
        self.ui.btn_sort_2.clicked.connect(self.sorting_algo)
        # scraping buttons
        self.web_scraping = WebScraping_thread()
        self.ui.btn_resume_scrap.clicked.connect(self.start_thread)
        self.ui.btn_pause_scrap.clicked.connect(self.stop_thread)
        self.ui.btn_clr_sort_2.clicked.connect(self.clear_sort)  # clear button of sorting
        self.changetextoflabel()

    def start_thread(self):
        self.web_scraping.stop_requested = False
        self.web_scraping.start()

    def stop_thread(self):
        self.web_scraping.stop()

    def clear_sort(self):    # clear bitton of sorting panel
        self.loaddata()
        self.loadtable(self.datas)

    def sorting_data(self):
        order = None
        algo = self.ui.combo_algo_sort_2.currentText()
        col = []
        count = 0
        if self.ui.radio_ascend_sort_2.isChecked():
            order = 'ascending'
        else:
            order = 'desending'
        if self.ui.col_name_2.isChecked():
            col.append('title')
            count+=1
        if self.ui.col_grade_2.isChecked():
            col.append('answers')
            count += 1
        if self.ui.col_year_2.isChecked():
            col.append('views')
            count += 1
        if self.ui.col_trans_2.isChecked():
            col.append('votes')
            count += 1
        if self.ui.col_mileage_2.isChecked():
            col.append('users')
            count += 1
        if self.ui.col_fuel_2.isChecked():
            col.append('reputation')
            count += 1
        if self.ui.col_cc_2.isChecked():
            col.append('time_stamp')
            count += 1
        if self.ui.col_link_2.isChecked():
            col.append('summary')
            count += 1
        return count, col, algo, order

    def sorting_algo(self):
        count, col, algo, order = self.sorting_data()
        for x in range(count):
            if algo == 'Bubble Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_Bubble_Sort(copy.deepcopy(self.datas), col[x]))
                else:
                    self.loadtable(des_sorting.dsc_Bubble_Sort(copy.deepcopy(self.datas), col[x]))
            if algo == 'Selection Sort ':
                if order == 'ascending':
                    self.loadtable(sorting.asc_selection_sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_selection_sort(self.datas, col[x]))
            if algo == 'Insertion Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_insertion_sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_insertion_sort(self.datas, col[x]))
            if algo == 'Merge Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_merge_sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_merge_sort(self.datas, col[x]))
            if algo == 'Quick Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_quick_Sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_quick_sort(self.datas, col[x]))
            if algo == 'Radix Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_radix_sort(self.datas, col[x], 10))
                else:
                    self.loadtable(des_sorting.desc_radix_sort(self.datas, col[x], 10))
            if algo == 'Bucket Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_bucket_sort_data(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_bucket_sort_data(self.datas, col[x]))
            if algo == 'Counting Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_counting_sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_counting_sort(self.datas, col[x]))
            if algo == 'Heap Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_heap_sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_heap_sort(self.datas, col[x]))
            if algo == 'Shell Sort':
                if order == 'ascending':
                    self.loadtable(sorting.asc_shell_sort(self.datas, col[x]))
                else:
                    self.loadtable(des_sorting.dsc_shell_sort(self.datas, col[x]))
            if algo == 'Comb Sort':
                if order == 'ascending':
                    data = sorting.asc_comb_sort(self.datas, col[x])
                    self.loadtable(data)
                else:
                    data = des_sorting.dsc_comb_sort(self.datas, col[x])
                    self.loadtable(data)

    def changetextoflabel(self):
        self.ui.col_name_2.setText('Title')
        self.ui.col_grade_2.setText('answers')
        self.ui.col_year_2.setText('views')
        self.ui.col_trans_2.setText('votes')
        self.ui.col_mileage_2.setText('Users')
        self.ui.col_fuel_2.setText('Reputation')
        self.ui.col_cc_2.setText('Time_stamp')
        self.ui.col_link_2.setText('Summary')

    def loadtable(self, loaddata):
        header_label = ['Title', 'No. of answer', 'No. of views', 'No. of votes', 'Tags', 'Reputation of User',
                        'Time Stamp', 'Summary']
        tabledata = []
        for x in range(len(loaddata.title)):
            data = [loaddata.title[x], str(loaddata.answers[x]), loaddata.views[x],
                    str(loaddata.votes[x]), loaddata.users[x], loaddata.reputation[x], loaddata.time_stamp[x],
                    loaddata.summary[x]]
            tabledata.append(data)
        table = self.ui.tableWidget
        table.setRowCount(len(tabledata))
        table.setColumnCount(len(tabledata[0]))
        table.setHorizontalHeaderLabels(header_label)
        for row_index, row_data in enumerate(tabledata):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                table.setItem(row_index, col_index, item)

    def loaddata(self):
        df = pd.read_csv("1.csv")
        datas = data()
        data.title = df['Title'].values.tolist()
        data.answers = df['No. of answers'].values.tolist()
        data.views = df['No. of views'].values.tolist()
        data.votes = df['No. of votes'].values.tolist()
        data.users = df['Users'].values.tolist()
        data.reputation = df['Reputation'].values.tolist()
        data.time_stamp = df['Time_stamp'].values.tolist()
        data.summary = df['Summary'].values.tolist()
        return data

    def toggle_frame(self):
        # Check the current visibility of the frame and toggle it
        frame = self.ui.frameSort
        if frame.isHidden():
            self.ui.frameSearch.hide()
            self.ui.frameScrap.hide()
            self.ui.framemain.hide()
            self.ui.tableWidget.show()
            frame.show()
        else:
            self.ui.tableWidget.hide()
            self.ui.framemain.show()
            frame.hide()

    def toggle_frame1(self):
        # Check the current visibility of the frame and toggle it
        frame = self.ui.frameSearch
        if frame.isHidden():
            self.ui.frameSort.hide()
            self.ui.frameScrap.hide()
            self.ui.framemain.hide()
            self.ui.tableWidget.show()
            frame.show()
        else:
            self.ui.tableWidget.hide()
            self.ui.framemain.show()
            frame.hide()

    def toggle_frame2(self):
        # Check the current visibility of the frame and toggle it
        frame = self.ui.frameScrap
        if frame.isHidden():
            self.ui.frameSort.hide()
            self.ui.frameSearch.hide()
            self.ui.framemain.hide()
            self.ui.tableWidget.hide()
            frame.show()
        else:
            self.ui.tableWidget.hide()
            self.ui.framemain.show()
            frame.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
