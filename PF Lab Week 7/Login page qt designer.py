<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(0, 85, 127);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>70</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>451</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 12pt &quot;Times New Roman&quot;;</string>
    </property>
    <property name="text">
     <string>UNIVERSITY OF ENGENNIRING AND TECHNOLOGY LAHORE</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>70</y>
      <width>141</width>
      <height>141</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>H:/1st Semester books UET CYS/Uet logo.png</pixmap>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>410</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(0, 255, 127);
font: 8pt &quot;MS Shell Dlg 2&quot;;
border: 2px solid rgb(0, 200, 100);
border-radius:15px;</string>
    </property>
    <property name="text">
     <string>LOGIN HERE</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>280</y>
      <width>71</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 10pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(255, 1, 1);</string>
    </property>
    <property name="text">
     <string>User name:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>330</y>
      <width>71</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 10pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(255, 0, 0);</string>
    </property>
    <property name="text">
     <string>Password:</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>280</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 57 8pt &quot;Roboto Medium&quot;;
border-radius: 15px;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>330</y>
      <width>141</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
    <property name="echoMode">
     <enum>QLineEdit::Password</enum>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>500</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
