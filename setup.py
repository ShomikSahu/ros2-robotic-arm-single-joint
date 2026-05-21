import os
from glob import glob
from setuptools import setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        ('share/' + package_name, ['package.xml']),

        # Install URDF files
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.urdf')
        ),

        # Install launch files
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='christ',
    maintainer_email='christ@ubuntu',
    description='My robot package',
    license='Apache-2.0',
    tests_require=['pytest'],

    entry_points={
        'console_scripts': [
            'my_robot_node = my_robot.my_robot_node:main',
            'publisher_node = my_robot.publisher_node:main',
            'subscriber_node = my_robot.subscriber_node:main',
        ],
    },
)