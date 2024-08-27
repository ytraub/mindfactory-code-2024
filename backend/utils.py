from pybricks.tools import StopWatch


class Timer:
    def __init__(self):
        self.stop_watch = StopWatch()
        self.last_tick = None

    def start(self):
        self.last_tick = self.stop_watch.time()

    def finished(self, duration: int) -> bool:
        now = self.stop_watch.time()
        diff = abs(self.last_tick - now)

        done = diff >= duration

        if done:
            self.last_tick = now

        return done

