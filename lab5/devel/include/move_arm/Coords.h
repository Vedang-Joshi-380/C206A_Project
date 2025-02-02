// Generated by gencpp from file move_arm/Coords.msg
// DO NOT EDIT!


#ifndef MOVE_ARM_MESSAGE_COORDS_H
#define MOVE_ARM_MESSAGE_COORDS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace move_arm
{
template <class ContainerAllocator>
struct Coords_
{
  typedef Coords_<ContainerAllocator> Type;

  Coords_()
    : y(0.0)
    , z(0.0)
    , theta(0.0)  {
    }
  Coords_(const ContainerAllocator& _alloc)
    : y(0.0)
    , z(0.0)
    , theta(0.0)  {
  (void)_alloc;
    }



   typedef double _y_type;
  _y_type y;

   typedef double _z_type;
  _z_type z;

   typedef double _theta_type;
  _theta_type theta;





  typedef boost::shared_ptr< ::move_arm::Coords_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::move_arm::Coords_<ContainerAllocator> const> ConstPtr;

}; // struct Coords_

typedef ::move_arm::Coords_<std::allocator<void> > Coords;

typedef boost::shared_ptr< ::move_arm::Coords > CoordsPtr;
typedef boost::shared_ptr< ::move_arm::Coords const> CoordsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::move_arm::Coords_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::move_arm::Coords_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::move_arm::Coords_<ContainerAllocator1> & lhs, const ::move_arm::Coords_<ContainerAllocator2> & rhs)
{
  return lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.theta == rhs.theta;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::move_arm::Coords_<ContainerAllocator1> & lhs, const ::move_arm::Coords_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace move_arm

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::move_arm::Coords_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::move_arm::Coords_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::move_arm::Coords_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::move_arm::Coords_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::move_arm::Coords_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::move_arm::Coords_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::move_arm::Coords_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4dfccfb48448aecffcee83ace2902cff";
  }

  static const char* value(const ::move_arm::Coords_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4dfccfb48448aecfULL;
  static const uint64_t static_value2 = 0xfcee83ace2902cffULL;
};

template<class ContainerAllocator>
struct DataType< ::move_arm::Coords_<ContainerAllocator> >
{
  static const char* value()
  {
    return "move_arm/Coords";
  }

  static const char* value(const ::move_arm::Coords_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::move_arm::Coords_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 y\n"
"float64 z\n"
"float64 theta\n"
;
  }

  static const char* value(const ::move_arm::Coords_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::move_arm::Coords_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.theta);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Coords_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::move_arm::Coords_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::move_arm::Coords_<ContainerAllocator>& v)
  {
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<double>::stream(s, indent + "  ", v.z);
    s << indent << "theta: ";
    Printer<double>::stream(s, indent + "  ", v.theta);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVE_ARM_MESSAGE_COORDS_H
