import bpy
import bgl


# def remap(value, leftMin, leftMax, rightMin, rightMax):
#     # Figure out how 'wide' each range is
#     leftSpan = leftMax - leftMin
#     rightSpan = rightMax - rightMin
#
#     # Convert the left range into a 0-1 range (float)
#     valueScaled = (value - leftMin) / leftSpan
#
#     # Convert the 0-1 range into a value in the right range.
#     return rightMin + valueScaled * rightSpan


def draw_callback_3d(points):
    # bgl.glDisable(bgl.GL_DEPTH_TEST)
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glPointSize(4)
    bgl.glLineWidth(3)

    for co, color in zip(points['co'], points['colors']):
        bgl.glColor4f(*color, 0.5)

        bgl.glBegin(bgl.GL_POINTS)
        bgl.glVertex3f(*co)

        bgl.glEnd()

    # Restore opengl defaults
    bgl.glPointSize(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)

    # bgl.glEnable(bgl.GL_DEPTH_TEST)
