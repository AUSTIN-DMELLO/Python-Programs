class FIFO:
    def __init__(self, frame_size):
        self.frame_size = frame_size
        self.frames = []
        self.page_faults = 0
        self.hits = 0
        self.total_accesses = 0
        self.last_insert_index = 0
    def page_replace(self, pages):
        for page in pages:
            self.total_accesses += 1
            if page not in self.frames:
                self.page_faults += 1
                if len(self.frames) == self.frame_size:
                    self.frames[self.last_insert_index] = page
                    self.last_insert_index = (self.last_insert_index + 1) % self.frame_size
                else:
                    self.frames.append(page)
                print(f"Page {page} loaded into frames: {self.frames}")
            else:
                self.hits += 1
                print(f"Page {page} already in frames: {self.frames}")
        print(f"Total Page Hits: {self.hits}")
        print(f"Total Page Misses: {self.page_faults}")
        print(f"Hit Ratio: {self.hits / self.total_accesses:.2f}")
        print(f"Miss Ratio: {(self.page_faults) / self.total_accesses:.2f}")
if __name__ == "__main__":
    page_sequence = input("Enter the sequence of pages (comma-separated): ").strip().split(",")
    pages = [int(page) for page in page_sequence]
    frame_size = int(input("Enter the frame size: "))
    fifo = FIFO(frame_size)
    fifo.page_replace(pages)