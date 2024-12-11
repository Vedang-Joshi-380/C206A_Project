;; Auto-generated. Do not edit!


(when (boundp 'move_arm::Coords)
  (if (not (find-package "MOVE_ARM"))
    (make-package "MOVE_ARM"))
  (shadow 'Coords (find-package "MOVE_ARM")))
(unless (find-package "MOVE_ARM::COORDS")
  (make-package "MOVE_ARM::COORDS"))

(in-package "ROS")
;;//! \htmlinclude Coords.msg.html


(defclass move_arm::Coords
  :super ros::object
  :slots (_y _z _theta ))

(defmethod move_arm::Coords
  (:init
   (&key
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:theta __theta) 0.0)
    )
   (send-super :init)
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _theta (float __theta))
   self)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:serialization-length
   ()
   (+
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _theta
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _theta
     (setq _theta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get move_arm::Coords :md5sum-) "4dfccfb48448aecffcee83ace2902cff")
(setf (get move_arm::Coords :datatype-) "move_arm/Coords")
(setf (get move_arm::Coords :definition-)
      "float64 y
float64 z
float64 theta

")



(provide :move_arm/Coords "4dfccfb48448aecffcee83ace2902cff")


