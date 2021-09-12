import React, { useState } from "react";
import styled from "styled-components";
import axios from "axios";
const RadioButtonWrapper = styled.div`
  background: rgb(255, 255, 255);
  box-shadow: 0 3px 6px rgba(87, 87, 87, 0.1), 0 3px 6px rgba(83, 83, 83, 0.23);
  flex-direction: row;
  width: 400px;
  border-radius: 20px;
  justify-content: center;
  align-items: center;
  height: 100px;
  margin: 0 auto;
`;

const Label = () => {
  const [inputStatus, setInputStatus] = useState("");
  const [sentiment, setSentiment] = useState([
    "행복",
    "슬픔",
    "놀람",
    "중립",
    "혐오",
    "분노",
    "공포"
  ]);

  const handleClickRadioButton = radioBtnName => {
    setInputStatus(radioBtnName);
  };
  const onSubmit = () => {
    axios({
      method: "post",
      url: "http://3.35.19.190/predict/label",
      data: { label: inputStatus },
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
    <>
      <RadioButtonWrapper>
        <h4>정답을 알려주세요!</h4>
        <p></p>
        {sentiment &&
          sentiment.map((sen, index) => (
            <>
              <input
                type="radio"
                key={index}
                id={sen}
                checked={inputStatus === sen}
                onClick={() => handleClickRadioButton(sen)}
              />
              <label htmlFor={sen}>{sen}</label>
            </>
          ))}
      </RadioButtonWrapper>
      <p></p>
      <button className="cv-btn" onClick={() => onSubmit()}>
        제출하기
      </button>
    </>
  );
};

export default Label;
