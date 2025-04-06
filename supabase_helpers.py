from supabase_config import supabase

def store_results(results):
    for index, row in results.iterrows():
        supabase.table("results").insert({
            "sample_id": int(row["id"]),
            "absorption_rate": float(row["absorption"]),
            "metal_level": float(row["metal"])
        }).execute()
