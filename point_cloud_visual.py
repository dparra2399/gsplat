import pycolmap
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QtAgg')

file_path = r'C:\Users\Patron\PycharmProjects\gsplat\cow gsplat\sfm\0'

reconstruction = pycolmap.Reconstruction(file_path)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


for point3D_id, point3D in reconstruction.points3D.items():
    if point3D_id > 900:
        continue
    ax.scatter(point3D.xyz[0], point3D.xyz[1], point3D.xyz[2], c='b', marker='o', s=10)


ax.set_ylim(2, 8)
ax.set_xlim(-4, 2)
ax.set_zlim(0, 4)
plt.show(block=True)
