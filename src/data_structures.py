def store_samples_in_map(data):
    sample_map = {}
    for index, row in data.iterrows():
        sample_id = f"sample{index+1:03d}"
        sample_map[sample_id] = {
            "metal": row["metal"],
            "absorption": row["absorption"]
        }
    return sample_map

def get_sample_by_id(sample_map, sample_id):
    return sample_map.get(sample_id, "Sample not found")
