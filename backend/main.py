from robot import Robot

robot = Robot()
# robot.main()

chain = robot.create_chain(
    [
        robot.tasks.drive_forward(10, 100),
        robot.tasks.drive_forward(10, 100),
        [robot.tasks.drive_forward(10, 100), robot.tasks.drive_forward(10, 100)]
    ]
)
