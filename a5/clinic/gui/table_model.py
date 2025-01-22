import sys
from PyQt6.QtCore import Qt, QAbstractTableModel



class TableModel(QAbstractTableModel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._data = []

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        headers = ['PHN', 'Name', 'Birthdate', 'Phone Number', 'Email', 'address']
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return '%s' % headers[section]
        return super().headerData(section, orientation, role)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        if self._data:
            return len(self._data[0])
        else:
            return 0

    def refresh_data(self):
        self._data = []
        patients = self.controller.list_patients()
        for i in range(len(patients)):
            patient = [str(patients[i].phn), patients[i].name, patients[i].birth_date, patients[i].phone, patients[i].email, patients[i].address]
            self._data.append(patient)
        self.layoutChanged.emit()

    def phn_search_table(self, patient):
        self._data = []
        result_patient = [str(patient.phn), patient.name, patient. birth_date, patient.phone, patient.email, patient.address]
        self._data.append(result_patient)
        self.layoutChanged.emit()

    def string_search_table(self, patients):
        self._data = []
        for i in range(len(patients)):
            patient = [str(patients[i].phn), patients[i].name, patients[i].birth_date, patients[i].phone, patients[i].email, patients[i].address]
            self._data.append(patient)
        self.layoutChanged.emit()

    def get_phn(self, i):
        return self._data[i][0]
    


    def data(self, index, role):
        value = self._data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            # Perform per-type checks and render accordingly.
            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value
            if isinstance(value, str):
                # Render strings with quotes
                return '%s' % value
            # Default (anything not captured above: e.g. int)
            return value

        if role == Qt.ItemDataRole.TextAlignmentRole:
            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight
