# Week 1.2, Session 2: Task 6
m_temp = int(input("Enter the machine's temperature in degrees Celsius: "))
m_pressure = int(input("Enter the machine's pressure in PSI: "))
operation_status = int("Enter the machine's operational status (1 for operating / 0 for stopped): ")

if m_temp > 80:
    print(f"ALERT: Machine temperature of {m_temp}\u00B0C  is too high! It is recommended to it shut down.")
elif 50 <= m_temp <= 80:
    print(f"Machine temperature of {m_temp}\u00B0C is within safe limits.")
else: 
    print(f"Machine temperature of {m_temp}\u00B0C is low. No further action is needed.")

if m_pressure > 100:
    print("ALERT: High temperature detected! Maintenance recommended.")
elif 70 <= m_pressure <= 100:
    print("Pressure is stable.")
else: 
    print("Pressure is low and the system is operating normally.")


if operation_status == 1:
    if m_temp > 80 or m_pressure > 100:
        print("ALERT: The machine is running in unsafe conditions and it is recommended to shut it down.")
    else:
        print("Machine is running normally.")
else:
    print("Machine has stopped and no immediate action is needed")



