import tools as tls
import tkinter as tk
import time

user = "sam"
password = "osinkii"

def zte_init(tl, port):
    tls.login_try(tl, user, password)
    
    sport = str(port)
    tls.send_taska(tl, "show port " + sport)
    tls.send_taska(tl, "show port " + sport + " statistics")
    tls.send_taska(tl, "show fdb port " + sport + " det")
    tls.send_taska(tl, "show mac dynamic port " + sport)
    tls.send_taska(tl, "show dhcp snooping binding port " + sport)

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

    #LINE 2
    def show_dhcp():
        tls.send_taska(tl, "show dhcp")
    def show_lease_all():
        tls.send_taska(tl, "show dhcp snooping binding")
    def show_log():
        tls.send_taska(tl, "show terminal log", 2)
    def show_all_down():
        tls.send_taska(tl, "show ports")

    #lINE 3
    def show_more():
        tls.send_task(tl, " ")
    def cancel():
        tls.send_taska(tl, "q")
    def interact():
        tl.interact()

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

    #LINE 2
    dhcp_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_dhcp)
    dhcp_t.grid(column=20, row=10, sticky='w')
    lease_all_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_lease_all)
    lease_all_t.grid(column=20, row=20, sticky='w')
    log_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_log)
    log_t.grid(column=20, row=30, sticky='w')
    all_down_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_all_down)
    all_down_t.grid(column=20, row=40, sticky='w')

    #LINE 3
    more_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=show_more)
    more_t.grid(column=30, row=10, sticky='w')
    cancel_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=cancel)
    cancel_t.grid(column=30, row=20, sticky='w')
    interact_t = tk.Button(window, text="Show link", font=("Helvetica", 10), command=interact)
    interact_t.grid(column=30, row=30, sticky='w')

    window.mainloop()