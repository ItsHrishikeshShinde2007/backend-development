Tracks = [
    {
        "Track_ID":1,
        "Track_Name":"Circuit de Monaco",
        "Elevation_Gain":44,
        "Elevation_Lost":44,
        "Max's_Avg_speed":171.18,
        "Max's_Top_Speed":292
    },
    {
        "Track_ID":2,
        "Track_Name":"Circuit De Spa Francorchamps",
        "Elevation_Gain":139,
        "Elevation_Lost":139,
        "Max's_Avg_speed":246.31,
        "Max's_Top_Speed":319
    },
    {
        "Track_ID":3,
        "Track_Name":"Las Vegas Strip Circuit",
        "Elevation_Gain":21,
        "Elevation_Lost":21,
        "Max's_Avg_speed":233.48,
        "Max's_Top_Speed":326
    },
    {
        "Track_ID":4,
        "Track_Name":"Bahrain International Circuit",
        "Elevation_Gain":17,
        "Elevation_Lost":17,
        "Max's_Avg_speed":217.15,
        "Max's_Top_Speed":323
    },
    {
        "Track_ID":5,
        "Track_Name":"Yas Marina Circuit",
        "Elevation_Gain":11,
        "Elevation_Lost":11,
        "Max's_Avg_speed":227.67,
        "Max's_Top_Speed":324.9
    }
]

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/tracks")
def get_all_tracks_first():
    return Tracks

@app.put("/tracks/{Track_ID}")
def update_track(Track_ID:int, updated_track:dict):
    for track in Tracks:
        if track["Track_ID"] == Track_ID:
            track.clear()
            track.update(updated_track)
            return{"Message":"Track data has been updated suvvessfully","Updated Track":track}
    raise HTTPException(status_code=404, detail={"Warning":"Track not found"})

               
@app.patch("/tracks/{Track_ID}")
def update_track_data(Track_ID:int, updated_track:dict):
    for track in Tracks:
        if track["Track_ID"] == Track_ID:
            track.update(updated_track)
            return{"Message":"The track has been updated successfully","Updated Track":track}
    raise HTTPException(status_code=404, detail={"Warning":"Track not found"})