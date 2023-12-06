from days.day import Day

class Range:

    def __init__(self, dest_start, source_start, length):
        self.dest_start = dest_start
        self.source_start = source_start
        self.length = length

    def includes(self, i):
        return i >= self.source_start and i < self.source_start + self.length

    def map(self, i):
        assert self.includes(i)
        return self.dest_start + (i - self.source_start)
    
    def reverse_includes(self, i):
        return i >= self.dest_start and i < self.dest_start + self.length
    
    def reverse_map(self, i):
        # assert self.reverse_includes(i)
        return self.source_start + (i - self.dest_start)

class Map:

    def __init__(self, blob):
        lines = blob.split("\n")
        self.name = lines[0].split()[0]
        self.name_from, _, self.name_to = self.name.split('-')
        ranges = [[int(n) for n in line.split()] for line in lines[1:]]
        self.ranges = [Range(*r) for r in ranges]
        
    def map(self, i):
        for r in self.ranges:
            if r.includes(i):
                return r.map(i)
        return i
    
    def reverse_map(self, i):
        for r in self.ranges:
            if r.reverse_includes(i):
                return r.reverse_map(i)
        return i
    
    # def find_range_including(self, i):
    #     for r in self.ranges:
    #         if r.includes(i):
    #             return r
            
    def max_dest_value(self):
        max_value = 0
        for r in self.ranges:
            max_value = max(max_value, r.dest_start + r.length)
        return max_value

class MapGroup:

    def __init__(self, maps):
        self.maps = maps
        self.reverse_maps = list(reversed(self.maps))
    
    # aka map_seed_to_location
    def map_all_the_way_through(self, i):
        for map in self.maps:
            i = map.map(i)
        return i
    
    def map_location_to_seed(self, i):
        for map in self.reverse_maps:
            i = map.reverse_map(i)
        return i

class Day5(Day):

    day = 5
    reuse_a_input_for_b = True

    def solve_a(self):
        seeds, *maps = self.input_blob.split('\n\n')
        seeds = [int(n) for n in seeds[len('seeds: '):].split()]
        print("creating maps")
        maps = [Map(map) for map in maps]
        print("creating map group")
        map_group = MapGroup(maps)
        print("mapping seeds")
        locations = [map_group.map_all_the_way_through(seed) for seed in seeds]
        print(min(locations))

    def solve_b(self):
        seed_nums, *maps = self.input_blob.split('\n\n')
        seed_nums = [int(n) for n in seed_nums[len('seeds: '):].split()]
        seed_ranges = [(seed_nums[i], seed_nums[i+1]) for i in range(0, len(seed_nums), 2)]
        # seed_Ranges = [Range(start, start, length) for start, length in seed_ranges]
        maps = [Map(map) for map in maps]
        map_group = MapGroup(maps)
        
        max_location = maps[-1].max_dest_value()
        CHUNK = 10000
        for rough_loc in range(0, max_location + 1, CHUNK):
            seed = map_group.map_location_to_seed(rough_loc)
            for sr_start, sr_length in seed_ranges:
                if seed >= sr_start and seed < sr_start + sr_length:
                    print(f"Rough seed: {seed}")
                    print(f"Rough location: {rough_loc}")
                    for loc in range(rough_loc - CHUNK, rough_loc + 1):
                        seed = map_group.map_location_to_seed(loc)
                        for sr_start, sr_length in seed_ranges:
                            if seed >= sr_start and seed < sr_start + sr_length:
                                print(f"seed: {seed}")
                                print(f"location: {loc}")
                                exit()
            if rough_loc % 1e7 == 0:
                print(f"Passed location {rough_loc:,} / {max_location:,} (invalid seed: {seed})")