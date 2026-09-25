class ZigbeeMessage:
    def __init__(self, message):
        self.raw = message

    def get_signal_level(self):
        value = self.raw.get('linkquality')
        try:
            return int(int(value) * 11 / 255)
        except (TypeError, ValueError):
            return None

    def get_battery_level(self):
        value = self.raw.get('battery')
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return None
