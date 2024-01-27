from pyglet.graphics import Group
from pyglet.math import Mat4, Vec2


class CameraGroup(Group):
    """ Graphics group emulating the behaviour of a camera in 2D space. """

    def __init__(self, window, game, x, y, zoom=1.0, order=0, parent=None):
        super().__init__(order, parent)
        self._window = window
        self.x = x
        self.y = y
        self.zoom = zoom
        self.game = game

    @property
    def position(self) -> Vec2:
        """Query the current offset."""
        return Vec2(self.x, self.y)

    @position.setter
    def position(self, new_position: Vec2):
        """Set the scroll offset directly."""
        self.x, self.y = new_position

    def set_state(self):
        """ Apply zoom and camera offset to view matrix. """

        # Translate using the offset.
        view_matrix = self._window.view.translate(-self.x * self.zoom, -self.y * self.zoom, 0)
        # Scale by zoom level.
        view_matrix = view_matrix.scale(self.zoom, self.zoom, 1)

        self._window.view = view_matrix

    def unset_state(self):
        """ Revert zoom and camera offset from view matrix. """
        # Since this is a matrix, you will need to reverse the translate after rendering otherwise
        # it will multiply the current offset every draw update pushing it further and further away.

        # Use inverse zoom to reverse zoom
        view_matrix = self._window.view.scale(1 / self.zoom, 1 / self.zoom, 1)
        # Reverse translate.
        view_matrix = view_matrix.translate(self.x * self.zoom, self.y * self.zoom, 0)

        self._window.view = view_matrix


class CenteredCameraGroup(CameraGroup):
    """ Alternative centered camera group.

    (0, 0) will be the center of the screen, as opposed to the bottom left.
    """

    def set_state(self):
        # Translate almost the same as normal, but add the center offset
        x = -self._window.width // 2 / self.zoom + self.x
        y = -self._window.height // 2 / self.zoom + self.y

        view_matrix = self._window.view.translate((-x * self.zoom, -y * self.zoom, 0))
        view_matrix = view_matrix.scale((self.zoom, self.zoom, 1))
        self._window.view = view_matrix

    def unset_state(self):

        x = -self._window.width // 2 / self.zoom + self.x
        y = -self._window.height // 2 / self.zoom + self.y

        view_matrix = self._window.view.scale((1 / self.zoom, 1 / self.zoom, 1))
        view_matrix = view_matrix.translate((x * self.zoom, y * self.zoom, 0))
        self._window.view = view_matrix