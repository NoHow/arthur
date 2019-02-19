import tools as tls
import tkinter as tk
import time
import underground as ug
import gw_proccessing as gwp

user = "sam"
password = "osinkii"

def zte_init(tl, sw_ip, port):
    tls.login_try(tl, user, password)
    time.sleep(1)
    
    sport = str(port)
    tls.send_taska(tl, "enable")
    tls.send_taska(tl, "rbnfqcrbqbynthyt")
    tls.send_taska(tl, "show port " + sport)
    tls.send_taska(tl, "show port " + sport + " statistics")
    tls.send_taska(tl, "show fdb port " + sport + " det")
    tls.send_taska(tl, "show mac dynamic port " + sport)
    tls.send_taska(tl, "show dhcp snooping binding port " + sport)

    gateway = gwp.get_connection(sw_ip)

    window = tk.Tk()
    window.title("ZTE | PORT: " + sport)
    
    #LINE 1
    def show_link():
        tls.send_taska(tl, "show port " + sport)
    def show_statistics():
        tls.send_taska(tl, "show port " + sport + " statistics")
    def show_mac():
        tls.send_taska(tl, "show fdb port " + sport + " det")
        tls.send_taska(tl, "show mac dynamic port " + sport)
    def show_lease():
        tls.send_taska(tl, "show dhcp snooping binding port " + sport)
    def test_cable():
        tls.send_taska(tl, "show vct port " + sport, 2)

    def port_off():
        tls.send_taska(tl, "set port " + sport + " disable")
    def port_on():
        tls.send_taska(tl, "set port " + sport + " enable")

    def dhcp_on():
        tls.send_taska(tl, "set dhcp snooping-and-option82 enable")
        tls.send_taska(tl, "set port $port acl " + sport + " dis")
        tls.send_taska(tl, "set dhcp port " +  sport + " client")
        tls.send_taska(tl, "set dhcp snooping add por t" + sport)
        tls.send_taska(tl, "set dhcp ip-source-guard add port " + sport)
        tls.send_taska(tl, "set dhcp option82 add port " + sport)
        tls.send_taska(tl, "set dhcp option82 sub-option port " + sport + " circuit-ID on cis")
    def dhcp_off():
        tls.send_taska(tl, "set dhcp snooping del port " + sport)
        tls.send_task(tl, "set dhcp ip-source-guard del port " + sport)
        tls.send_taska(tl, "set dhcp option82 del port " + sport)

    #LINE 2
    def show_dhcp():
        tls.send_taska(tl, "show dhcp")
    def show_lease_all():
        tls.send_taska(tl, "show dhcp snooping binding")
    def show_log():
        tls.send_taska(tl, "show terminal log", 2)
    def show_all_down():
        tls.send_taska(tl, "show ports")
    
    def neigh_port_boot():
        tls.send_taska(tl, "set port " + switch_port_data.get() + " disable")
        time.sleep(4)
        tls.send_taska(tl, "set port " + switch_port_data.get() + " enable")

    #lINE 3
    def show_more():
        tls.send_taska(tl, " ")
    def cancel():
        tls.send_taska(tl, "q")
    def interact():
        tl.interact()

    #LINE GATEWAY
    def show_arp_by_mac():
        gwp.show_arp_by_mac(gateway['connection'], gateway['vendor'], mac_data.get())

    #LINE 1
    link_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_link)
    link_t.grid(column=10, row=10, sticky='w')
    stat_t = tk.Button(window, text="Show stat", font=("Helvetica", 10), command=show_statistics)
    stat_t.grid(column=10, row=20, sticky='w')
    mac_t = tk.Button(window, text="Show mac", font=("Helvetica", 10), command=show_mac)
    mac_t.grid(column=10, row=30, sticky='w')
    lease_t = tk.Button(window, text="Show lease", font=("Helvetica", 10), command=show_lease)
    lease_t.grid(column=10, row=40, sticky='w')
    cable_t = tk.Button(window, text="Cable test", font=("Helvetica", 10), command=test_cable)
    cable_t.grid(column=10, row=50, sticky='w')

    line = tk.Label(window, text="-----", font=("Helvetica", 10))
    line.grid(column=10, row=60, sticky='w', pady='0.3m')

    link_t = tk.Button(window, text="Port on", font=("Helvetica", 10), command=port_on)
    link_t.grid(column=10, row=70, sticky='w')
    link_t = tk.Button(window, text="Port off", font=("Helvetica", 10), command=port_off)
    link_t.grid(column=10, row=80, sticky='w')

    line = tk.Label(window, text="-----", font=("Helvetica", 10))
    line.grid(column=10, row=90, sticky='w', pady='0.3m')

    dchp_t = tk.Button(window, text="DHCP", font=("Helvetica", 10), command=dhcp_on)
    dchp_t.grid(column=10, row=100, sticky='w')
    static_t = tk.Button(window, text="STATIC", font=("Helvetica", 10), command=dhcp_off)
    static_t.grid(column=15, row=100, sticky='w')

    #LINE 2
    dhcp_t = tk.Button(window, text="Show dhcp", font=("Helvetica", 10), command=show_dhcp)
    dhcp_t.grid(column=20, row=10, sticky='w')
    lease_all_t = tk.Button(window, text="Show lease all", font=("Helvetica", 10), command=show_lease_all)
    lease_all_t.grid(column=20, row=20, sticky='w')
    log_t = tk.Button(window, text="Show log", font=("Helvetica", 10), command=show_log)
    log_t.grid(column=20, row=30, sticky='w')
    all_down_t = tk.Button(window, text="Show DOWN", font=("Helvetica", 10), command=show_all_down)
    all_down_t.grid(column=20, row=40, sticky='w')

    line = tk.Label(window, text="-----", font=("Helvetica", 10))
    line.grid(column=20, row=50, sticky='w', pady='0.3m')

    link_t = tk.Button(window, text="Sosed Port reboot", font=("Helvetica", 10), command=neigh_port_boot)
    link_t.grid(column=20, row=60, sticky='w')
    switch_port_data = tk.Spinbox(window, from_=1, to=64, font=("Helvetica", 10), width=5)
    switch_port_data.grid(column=25, row=60, sticky='w')

    #LINE 3
    more_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_more)
    more_t.grid(column=30, row=10, sticky='w')
    cancel_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=cancel)
    cancel_t.grid(column=30, row=20, sticky='w')
    interact_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=interact)
    interact_t.grid(column=30, row=30, sticky='w')

    #GW LINE
    link_t = tk.Button(window, text="Show arp", font=("Helvetica", 10), command=show_arp_by_mac)
    link_t.grid(column=40, row=10, sticky='w')
    mac_data = tk.Spinbox(window, from_=1, to=64, font=("Helvetica", 10), width=15)
    mac_data.grid(column=45, row=10, sticky='w')

    window.mainloop()


#CISCO
def cisco_init(tl, sw_ip, port):
    tls.login_try(tl, user, password)
    
    sport = 'e' + str(port)
    tls.send_taska(tl, "show interface status ethernet " + sport)
    tls.send_taska(tl, "show interface counters ethernet " + sport)
    tls.send_taska(tl, "show interface configuration ethernet " + sport)
    tls.send_taska(tl, "show mac address-table ethernet " + sport)
    tls.send_taska(tl, "show ip dhcp snooping binding ethernet " + sport)

    gateway = gwp.get_connection(sw_ip)

    window = tk.Tk()
    window.title("CISCO | PORT: " + sport)
    
    #LINE 1
    def show_link():
        tls.send_taska(tl, "show interface status ethernet " + sport)
    def show_admin():
        tls.send_taska(tl, "show interface configuration ethernet " + sport)
    def show_description():
        tls.send_taska(tl, "show interface description ethernet " + sport)
    def show_statistics():
        tls.send_taska(tl, "show interface counters ethernet " + sport)
    def show_mac():
        tls.send_taska(tl, "show mac address-table ethernet " + sport)
    def show_lease():
        tls.send_taska(tl, "show ip dhcp snooping binding ethernet " + sport)
    def test_cable():
        tls.send_taska(tl, "test copper-port tdr " + sport, 2)

    def port_off():
        tls.send_task(tl, "configurtion")
        tls.send_task(tl, "interface ethernet " + sport)
        tls.send_task(tl, "shutdown")
        tls.send_taska(tl, "end")
    def port_on():
        tls.send_task(tl, "configurtion")
        tls.send_task(tl, "interface ethernet " + sport)
        tls.send_task(tl, "no shutdown")
        tls.send_taska(tl, "end")

    def dhcp_on():
        tls.send_task(tl, "ip dhcp snooping")
        tls.send_task(tl, "ip dhcp information option")
        tls.send_task(tl, "no ip dhcp snooping database")
        tls.send_task(tl, "ip dhcp snooping vlan " + vlan_data_bind.get())
        tls.send_task(tl, "ip arp inspection")
        tls.send_task(tl, "ip arp inspection validate")
        tls.send_task(tl, "ip arp inspection vlan " + vlan_data_bind.get())
        tls.send_task(tl, "ip source-guard")
        tls.send_task(tl, "configure")
        tls.send_task(tl, "interface ethernet" + sport)
        tls.send_task(tl, "ip source-guard")
        tls.send_task(tl, "no ip arp inspection trust")
        tls.send_task(tl, "no ip dhcp snooping trust")
        tls.send_taska(tl, "end")
    def static_bind():
        tls.send_task(tl, "configure")
        tls.send_taska(tl, "ip source-guard binding " + mac_data_bind.get() + " " + vlan_data_bind.get() + " " +  ip_data_bind.get() + " ethernet " + sport)
        tls.send_taska(tl, "end")
    def static_bind_remove():
        tls.send_task(tl, "configure")
        tls.send_taska(tl, "no ip source-guard binding " + mac_data_bind.get() + " " + vlan_data_bind.get())
        tls.send_taska(tl, "end")

    #LINE 2
    def show_lease_all():
        tls.send_taska(tl, "show ip dhcp snooping binding")
    def show_log():
        tls.send_taska(tl, "show log", 2)
    def show_all_down():
        tls.send_taska(tl, "show interface configuration")
    def neigh_port_boot():
        tls.send_task(tl, "configurtion")
        tls.send_taska(tl, "interface ethernet " + 'e' + switch_port_data.get())
        tls.send_taska(tl, "shutdown")
        time.sleep(4)
        tls.send_taska(tl, "no shutdown")

    #lINE 3
    def show_more():
        tls.send_taska(tl, " ")
    def cancel():
        tls.send_taska(tl, "q")
    def interact():
        tl.interact()

    #LINE GATEWAY
    def show_arp_by_mac():
        gwp.show_arp_by_mac(gateway['connection'], gateway['vendor'], mac_data.get())

    #LINE 1
    link_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_link)
    link_t.grid(column=10, row=10, sticky='w')
    admin_t = tk.Button(window, text="Show admin", font=("Helvetica", 10), command=show_admin)
    admin_t.grid(column=10, row=20, sticky='w')
    desc_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_description)
    desc_t.grid(column=10, row=30, sticky='w')
    stat_t = tk.Button(window, text="Show stat", font=("Helvetica", 10), command=show_statistics)
    stat_t.grid(column=10, row=40, sticky='w')
    mac_t = tk.Button(window, text="Show mac", font=("Helvetica", 10), command=show_mac)
    mac_t.grid(column=10, row=50, sticky='w')
    lease_t = tk.Button(window, text="Show lease", font=("Helvetica", 10), command=show_lease)
    lease_t.grid(column=10, row=60, sticky='w')
    cable_t = tk.Button(window, text="Cable test", font=("Helvetica", 10), command=test_cable)
    cable_t.grid(column=10, row=70, sticky='w')

    line = tk.Label(window, text="-----", font=("Helvetica", 10))
    line.grid(column=10, row=80, sticky='w', pady='0.3m')

    porton_t = tk.Button(window, text="Port on", font=("Helvetica", 10), command=port_on)
    porton_t.grid(column=10, row=90, sticky='w')
    portoff_t = tk.Button(window, text="Port off", font=("Helvetica", 10), command=port_off)
    portoff_t.grid(column=10, row=100, sticky='w')

    line2 = tk.Label(window, text="-----", font=("Helvetica", 10))
    line2.grid(column=10, row=110, sticky='w', pady='0.3m')

    dhcp_t = tk.Button(window, text="DHCP config", font=("Helvetica", 10), command=dhcp_on)
    dhcp_t.grid(column=10, row=120, sticky='w')

    static_bind = tk.Button(window, text="Static bind", font=("Helvetica", 10), command=static_bind)
    static_bind.grid(column=10, row=120, sticky='w')
    static_bind_remove = tk.Button(window, text="Static bind", font=("Helvetica", 10), command=static_bind_remove)
    static_bind_remove.grid(column=15, row=120, sticky='w')
    mac_info_bind = tk.Label(window, text="MACb", font=("Helvetica", 10))
    mac_info_bind.grid(column=10, row=130, sticky='w')
    mac_data_bind = tk.Spinbox(window, font=("Helvetica", 10), width=5)
    mac_data_bind.grid(column=15, row=130, sticky='w')
    mac_data_bind.insert(0, "ff:ff:ff:ff:ff:ff")
    ip_info_bind = tk.Label(window, text="IPb", font=("Helvetica", 10))
    ip_info_bind.grid(column=10, row=140, sticky='w')
    ip_data_bind = tk.Spinbox(window, font=("Helvetica", 10), width=5)
    ip_data_bind.grid(column=15, row=140, sticky='w')
    vlan_info_bind = tk.Label(window, text="VLANb", font=("Helvetica", 10))
    vlan_info_bind.grid(column=10, row=150, sticky='w')
    vlan_data_bind = tk.Spinbox(window, font=("Helvetica", 10), width=5)
    vlan_data_bind.grid(column=15, row=150, sticky='w')
    
    #LINE 2
    lease_all_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_lease_all)
    lease_all_t.grid(column=20, row=10, sticky='w')
    log_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_log)
    log_t.grid(column=20, row=20, sticky='w')
    all_down_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_all_down)
    all_down_t.grid(column=20, row=30, sticky='w')

    line = tk.Label(window, text="-----", font=("Helvetica", 10))
    line.grid(column=20, row=40, sticky='w', pady='0.3m')

    link_t = tk.Button(window, text="Sosed Port reboot", font=("Helvetica", 10), command=neigh_port_boot)
    link_t.grid(column=20, row=50, sticky='w')
    switch_port_data = tk.Spinbox(window, from_=1, to=64, font=("Helvetica", 10), width=5)
    switch_port_data.grid(column=25, row=50, sticky='w')

    #LINE 3
    more_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_more)
    more_t.grid(column=30, row=10, sticky='w')
    cancel_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=cancel)
    cancel_t.grid(column=30, row=20, sticky='w')
    interact_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=interact)
    interact_t.grid(column=30, row=30, sticky='w')

    #GW LINE
    link_t = tk.Button(window, text="Show arp", font=("Helvetica", 10), command=show_arp_by_mac)
    link_t.grid(column=40, row=10, sticky='w')
    mac_data = tk.Spinbox(window, from_=1, to=64, font=("Helvetica", 10), width=15)
    mac_data.grid(column=45, row=10, sticky='w')

    window.mainloop()