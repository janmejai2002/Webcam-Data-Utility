#!/usr/bin/env python3

class roi:
    def __init__(self, roi_x, roi_y, roi_h, roi_w, frame_base, movement_steps, size_change_steps):
        self.x, self.y, self.h, self.w = roi_x, roi_y, roi_h, roi_w
        self.frame_y,self.frame_x=frame_base.shape[:2]
        self.steps = movement_steps
        self.size_steps = size_change_steps

    def display_val(self):
        return f"x : {self.x}, y : {self.y}, h : {self.h}, w : {self.w}"

    def moveup(self):
        self.y -= self.steps

    def movedown(self):
        self.y += self.steps

    def moveleft(self):
        self.x -= self.steps

    def moveright(self):
        self.x += self.steps

    def create_box(self):
        A = (self.x, self.y)
        C = (self.x - self.w, self.y - self.h)
        return A, C

    def check_all(self):
        if self.y < 50:
            self.y = 50

        if self.y > self.frame_y:
            self.y = self.frame_y

        if self.x < 50:
            self.x = 50

        if self.x > self.frame_x:
            self.x = self.frame_x

        if self.w > self.frame_x:
            self.w = self.frame_x

        if self.h > self.frame_y:
            self.h = self.frame_y

        if self.w < 50:
            self.w = 50

        if self.h < 50:
            self.h = 50

        if self.x - self.w <0:
            self.x = self.w

        if self.y - self.h < 0:
            self.y =self.h

    def increase_size(self):
        self.h += self.size_steps
        self.w += self.size_steps

    def decrease_size(self):
        self.h -= self.size_steps
        self.w -= self.size_steps

    def restore_shape(self):
        self.h = self.frame_x//5
        self.w = self.frame_x//5
        self.x = self.frame_x//2
        self.y = self.frame_x//2

    def create_roi_zone(self):
        # format [y1,y2,x1,x2]
        y1 = self.y - self.h
        y2 = self.y
        x1 = self.x - self.w
        x2 = self.x
        return [y1, y2, x1, x2]

    def action_control(self, key):
        if key == ord('w'):
            self.moveup()
        elif key == ord('s'):
            self.movedown()
        elif key == ord('a'):
            self.moveleft()
        elif key == ord('d'):
            self.moveright()
        elif key == ord('i'):
            self.increase_size()
        elif key == ord('k'):
            self.decrease_size()
        elif key == ord('r'):
            self.restore_shape()
        else:
            pass
