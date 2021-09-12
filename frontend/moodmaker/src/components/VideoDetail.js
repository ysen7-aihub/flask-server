import React from "react";

const VideoDetail = ({ video }) => {
  /*
  console.log(video);
  if (!video) {
    return <div>Loading...</div>;
  }
  */

  //const videoId = video.id.videoId;
  //const src = `https://www.youtube.com/embed/${videoId}`;
  const src = "https://www.youtube.com/embed/tgbNymZ7vqY";
  return (
    <div className="video-container">
      <iframe className="responsive-iframe" src={src}></iframe>
      <div className="details">{/* <div>{video.snippet.title}</div> */}</div>
    </div>
  );
};

export default VideoDetail;
