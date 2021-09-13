import React, { useState } from "react";
import VideoDetail from "./VideoDetail";
import YoutubeSearch from "youtube-api-search";
import dotenv from "dotenv";

function Music({ content }) {
  const [selectedVideo, set__selectedVideo] = useState();

  const videoSearch = term => {
    dotenv.config();
    YoutubeSearch({ key: process.env.API_KEY, term: term }, videos => {
      set__selectedVideo(videos[0]);
    });
    return <VideoDetail video={selectedVideo} />;
  };

  return (
    <div id="m-container">
      <div className="s-heading"></div>

      <div className="video">
        {content &&
          content.map((data, index) => (
            <li key={index}>
              <h3>{data.artist + " - " + data.name}</h3>
              {/*{videoSearch(data.artist + " - " + data.name)}*/}
              <VideoDetail video={data.src} />
            </li>
          ))}
      </div>
    </div>
  );
}

export default Music;
