cmake_minimum_required(VERSION 2.8)
project( ColorImage )
find_package( OpenCV )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( ColorImage ColorImage.cpp )
target_link_libraries( ColorImage ${OpenCV_LIBS} )

cmake_minimum_required(VERSION 2.8)
project( Noise )
find_package( OpenCV )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( Noise Noise.cpp )
target_link_libraries( Noise ${OpenCV_LIBS} )

cmake_minimum_required(VERSION 2.8)
project( Threshold )
find_package( OpenCV )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( Threshold Threshold.cpp )
target_link_libraries( Threshold ${OpenCV_LIBS} )