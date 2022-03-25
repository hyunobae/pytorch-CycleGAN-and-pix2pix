import matplotlib.pyplot as plt
import numpy as np

# loss_GA = D_A(G_A(A)) loss_GB = D_B(G_B(B)) cycleA = recA, realA cycleB = recB, realB
# idtA = ||G_A(B) - B||
cnt = 0
epoch = 0
array = []
small_arr = []

ecnt = 0
pflag=0
f, axex = plt.subplots(2, 4)
f.set_size_inches((60, 40))

mda, mdb, mcya, mcyb, mida, midb, mga, mgb = 0, 0, 0, 0, 0, 0, 0, 0
nda, ndb, ncya, ncyb, nida, nidb, nga, ngb = 3, 3, 3, 3, 3, 3, 3, 3

rm = [8, 16, 24, 32 ,40, 48, 56, 64, 72, 80, 88, 96]
with open('D:/cycleoriginal/checkpoints/maps_cyclegan/loss_log.txt', 'r') as file:
    for text in file:
        iter = text.find("iters:")
        cnt += 1
        try:
            pflag=0
            iter = int(text[iter+7:iter+9]) # 두자리수 iter
        except ValueError:
            try:
                pflag=0
                iter = int(text[iter+7:iter+8])#한자리수 iter

            except ValueError:
                try:
                    iter = int(text[iter+7:iter+10])
                except ValueError:
                    try:
                        iter = int(text[iter+7:iter+11])
                    except ValueError:
                        pass

        if iter in rm:
            print(iter)
            cnt -= 1

        elif cnt==5:
            print('in')
            # if epoch % 10 == 0 or epoch == 1:
            #     print(epoch)
            da = text.find("D_A")
            da = float(text[da + 5:da + 10])

            ga = text.find("G_A")
            ga = float(text[ga + 5:ga + 10])

            cya = text.find("cycle_A")
            cya = float(text[cya + 9:cya + 14])

            idta = text.find("idt_A")
            idta = float(text[idta + 7:idta + 12])

            db = text.find("D_B")
            db = float(text[db + 5:db + 10])

            gb = text.find("G_B")
            gb = float(text[gb + 5:gb + 10])

            cyb = text.find("cycle_B")
            cyb = float(text[cyb + 9:cyb + 14])

            idtb = text.find("idt_B")
            idtb = float(text[idtb + 7:idtb + 12])

            if mda < da: mda = da
            if nda > da: nda = da
            if mdb < db: mdb = db
            if ndb > db: ndb = db
            if mcya < cya: mcya = cya
            if ncya > cya: ncya = cya
            if mcyb < cyb: mcyb = cyb
            if ncyb > cyb: ncyb = cyb
            if mga < ga: mga = ga
            if nga > ga: nga = ga
            if mgb < gb: mgb = gb
            if ngb > gb: ngb = gb
            if mida < idta: mida = idta
            if nida > idta: nida = idta
            if midb < idtb: midb = idtb
            if nidb > idtb: nidb = idtb

            array.append((da, ga, cya, idta, db, gb, cyb, idtb))
            cnt=0



axex[0, 0].set_ylim([nda, mda])
axex[0, 1].set_ylim([nga, mga])
axex[0, 2].set_ylim([ncya, mcya])
axex[0, 3].set_ylim([nida, mida])
axex[1, 0].set_ylim([ndb, mdb])
axex[1, 1].set_ylim([ngb, mgb])
axex[1, 2].set_ylim([ncyb, mcyb])
axex[1, 3].set_ylim([nidb, midb])

for epoch, arr in enumerate(array):
    axex[0, 0].set_title('loss DA')
    axex[0, 0].plot(epoch, arr[0], 'r', label='dA', marker='.', linestyle='--')

    axex[1, 0].set_title('loss DB')
    axex[1, 0].plot(epoch, arr[4], 'b', label='dB', marker='v', linestyle='--')

    axex[0, 1].set_title('loss GA')
    axex[0, 1].plot(epoch, arr[1], 'r', label='gA', marker='.', linestyle='--')

    axex[1, 1].set_title('loss GA')
    axex[1, 1].plot(epoch, arr[5], 'b', label='gB', marker='v', linestyle='--')

    axex[0, 2].set_title('loss cycleA')
    axex[0, 2].plot(epoch, arr[2], 'r', label='cycleA', marker='.', linestyle='--')

    axex[1, 2].set_title('loss cycleB')
    axex[1, 2].plot(epoch, arr[6], 'b', label='cycleB', marker='v', linestyle='--')

    axex[0, 3].set_title('loss identityA')
    axex[0, 3].plot(epoch, arr[3], 'r', label='idtA', marker='.', linestyle='--')

    axex[1, 3].set_title('loss identityB')
    axex[1, 3].plot(epoch, arr[7], 'b', label='idtB', marker='v', linestyle='--')

plt.show()
