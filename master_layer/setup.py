from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=[],
    package_dir={},
    requires=['rospy', 'geometry_msgs']
)

setup(**setup_args)
