import React, { useRef, useState } from "react";
import API from "../utils/api";
import axios from "axios";
function UploadText({ history }) {
  const textAreaRef = useRef(null);

  function handleTa(e) {
    e.preventDefault();
    setIsShow(!isShow);
  }
  const [isShow, setIsShow] = useState(false);
  const [txt, setTxt] = useState("");

  const onChange = e => {
    setTxt(e.target.value);
    // console.log(value);
  };

  const onSubmitText = async () => {
    await axios({
      method: "post",
      url: "http://3.35.19.190/diary/txt",
      data: { txt: txt },
      headers: { "Content-Type": "application/json" },
      timeout: 100000
    })
      .then(response => {
        console.log(response);
      })
      .catch(response => {
        console.log(response);
      });
  };

  return (
    <div className="main">
      <div id="features">
        <div className="photo">
          <div className="features-text">
            <h2>일기를 업로드하세요</h2>
            <h3></h3>
            <p>
              아래 버튼을 눌러
              <br />
              <br />
              오늘의 일기를 작성해보세요
            </p>
            <form onSubmit={() => onSubmitText}>
              <div className="b-container">
                <div>
                  {!isShow && (
                    <button className="cv-btn" onClick={handleTa}>
                      + 일기 쓰러가기
                    </button>
                  )}
                </div>
                <div>
                  {isShow && (
                    <textarea
                      className="ta"
                      type="text"
                      value={txt}
                      onChange={onChange}
                      ref={textAreaRef}
                      maxLength="200"
                    />
                  )}
                </div>
              </div>
              <button>취소</button>
              <button
                type="submit"
                onClick={() => {
                  onSubmitText();
                  history.push("/uploadphoto");
                }}
              >
                다음
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UploadText;
