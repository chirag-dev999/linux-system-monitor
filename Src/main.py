import sys
from collections import deque
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
import pyqtgraph as pg

from cpu     import get_cpu_usage
from memory  import get_memory_usage
from process import get_processes
from gpu_temp import get_gpu_temp
from gpu    import get_gpu_usage
from in_gpu import get_ingpu_usage
from uptime import get_uptime
pg.setConfigOptions(antialias=True)

HISTORY = 60


def make_label(text, size=10, color="#C9C9C9"):
    lbl = QLabel(text)
    lbl.setFont(QFont("Consolas", size))
    lbl.setStyleSheet(f"color: {color};")
    return lbl


def make_chart(title, color):
    chart = pg.PlotWidget(title=title)
    chart.setBackground("#000000")
    chart.showGrid(x=True, y=True, alpha=0.3)
    chart.setYRange(0, 100)
    chart.hideButtons()
    chart.setMenuEnabled(False)
    curve = chart.plot([0] * HISTORY, pen=pg.mkPen(color=color, width=2))
    return chart, curve


class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Monitor")
        self.setMinimumSize(900, 600)
        self.setWindowIcon(QtGui.QIcon('/home/chirag/linux-monitor/assets/icon.png'))
        self.setStyleSheet("background-color: #000000")

        self.cpu_history = deque([0.0] * HISTORY, maxlen=HISTORY)
        self.gpu_history = deque([0.0] * HISTORY, maxlen=HISTORY)
        self.mem_history = deque([0.0] * HISTORY, maxlen=HISTORY)
        self.ingpu_history = deque([0.0] * HISTORY, maxlen=HISTORY)
        self.temp_history = deque([0.0] * HISTORY, maxlen=HISTORY)

        # warm up CPU delta
        get_cpu_usage()

        self.build_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        layout.addWidget(make_label("System Monitor", size=14, color="#D8D8D8"))

        stats_row = QHBoxLayout()
        self.lbl_cpu  = make_label("CPU: --%",      color="#fff200")
        self.lbl_ingpu  = make_label("Integrated GPU: --%",      color="#00ff84")
        self.lbl_gpu  = make_label("GPU: --%",      color="#00821c")
        self.lbl_gtemp = make_label("GPU temperature: --", color="#ff7b00")
        self.lbl_mem  = make_label("MEM: --%",      color="#00a2d4")
        self.lbl_proc = make_label("Processes: --", color="#ff00a2")
        self.lbl_upt= make_label("uptime: --", color="#8f00a4")

        for lbl in (self.lbl_cpu, self.lbl_gpu, self.lbl_gtemp, self.lbl_ingpu, self.lbl_mem, self.lbl_proc, self.lbl_upt):
            stats_row.addWidget(lbl)
        stats_row.addStretch()
        layout.addLayout(stats_row)

        grid = QGridLayout()
        grid.setSpacing(10)

        cpu_chart,  self.cpu_curve  = make_chart("CPU Usage (%)",    "#fff200")
        gpu_chart,  self.gpu_curve  = make_chart("GPU Usage (%)",    "#00821c")
        ingpu_chart, self.ingpu_curve = make_chart("INTEGRATED GPU Usage (%)",     "#00ff84")
        mem_chart,  self.mem_curve  = make_chart("Memory Usage (%)", "#00a2d4")

        grid.addWidget(cpu_chart,  0, 0)
        grid.addWidget(gpu_chart,  0, 1)
        grid.addWidget(ingpu_chart, 1, 0)
        grid.addWidget(mem_chart,  1, 1)

        layout.addLayout(grid)

    def update_stats(self):
        cpu = get_cpu_usage()
        self.cpu_history.append(cpu)
        self.lbl_cpu.setText(f"CPU: {cpu}%")
        self.cpu_curve.setData(list(self.cpu_history))

        gpu = get_gpu_usage()
        self.gpu_history.append(gpu)
        self.lbl_gpu.setText(f"GPU: {gpu}%")
        self.gpu_curve.setData(list(self.gpu_history))

        temp = get_gpu_temp()
        self.temp_history.append(temp)
        self.lbl_gtemp.setText(f"GPU temp: {temp} \N{DEGREE SIGN}C")

        ingpu= get_ingpu_usage()
        self.ingpu_history.append(ingpu)
        self.lbl_ingpu.setText(f"Integrated GPU {ingpu}%")
        self.ingpu_curve.setData(list(self.ingpu_history))

        mem = get_memory_usage()
        self.mem_history.append(mem)
        self.lbl_mem.setText(f"MEM: {mem}%")
        self.mem_curve.setData(list(self.mem_history))

        running, total = get_processes()
        self.lbl_proc.setText(f"Processes: {running} / {total}")

        hours, minutes= get_uptime()
        self.lbl_upt.setText(f"Uptime: {hours} hours {minutes} mins")

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SystemMonitor()
    win.show()
    sys.exit(app.exec_())
