# 🚨 Suicide Prevention System using Arduino Uno

## 💡 Project Overview

This is a **Suicide Prevention System** built using the **Arduino Uno**, aimed at saving lives by detecting potential suicide attempts in real-time. The system uses a **load sensor** to detect when someone steps onto a specific high-risk zone (like a bridge edge or railway platform), and triggers a **buzzer** alarm to alert people nearby.

---

## ⚙️ How It Works

- The **load sensor** detects weight placed on it.
- If the weight crosses a certain threshold, the **Arduino Uno** activates a **buzzer**.
- The buzzer creates an immediate alert, helping others intervene quickly.

---

## 🛠️ Components Used

| Component           | Quantity |
|---------------------|----------|
| Arduino Uno         | 1        |
| Load Sensor (HX711) | 1        |
| Buzzer              | 1        |
| Connecting Wires    | As needed |
| Power Supply        | 1        |

---

## 💻 Arduino Code

The complete code is available in the `code.ino` file included in this project folder.

### Main Features:
- Reads real-time weight from load sensor
- Triggers buzzer if weight > threshold
- Simple and effective early warning system

---

## 🚀 Setup Instructions

1. Connect the **load sensor** and **buzzer** to the Arduino Uno.
2. Upload the code to Arduino using the Arduino IDE.
3. Power the Arduino using USB or external adapter.
4. Test the system by stepping or placing weight on the sensor.

---

## 🔧 Possible Future Upgrades

- Add GSM or Wi-Fi module to send real-time alerts to family or authorities.
- Connect with a web dashboard for live monitoring.
- Use cameras or AI for better detection in high-traffic areas.

---

## 🙌 Motivation

Even simple systems can make a difference. This project is a step toward **mental health support** through low-cost, real-time suicide prevention technology.

---

## 👤 Author

Made with care by  
**[Arvind S Iyer]**  
First-Year Engineering Student  
**Pimpri Chinchwad College of Engineering and Research (PCCOER)**

