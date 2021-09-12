import React from "react";
import Dropzone from "./dropzone";

function UploadPhoto(props) {
  return (
    <div className="main">
      <div id="features">
        <div className="photo">
          <div className="features-text">
            <h2>오늘의 감정에 맞는 사진을 업로드하세요</h2>
            <p>
              <br />
              <b>01</b> 하늘이 나온 풍경, 배경, 날씨 사진만 가능합니다.
              <br />
              <br />
              <b>02</b> 파일 확장자는 jpg, jpeg, png만 가능합니다.
              <br />
              <br />
              <b>03</b> 업로드한 사진은 딥러닝 모델을 학습하는데 사용될 수
              있습니다.
              <br />
              <br />
            </p>

            <div className="b-container">
              <Dropzone />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UploadPhoto;
