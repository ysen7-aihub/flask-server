import React, { useCallback } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { useDropzone } from "react-dropzone";

export default function Dropzone() {
  const onDrop = useCallback(async acceptedFiles => {
    const formData = new FormData();

    formData.append("img", acceptedFiles[0]);
    console.log(acceptedFiles[0]);

    const config = {
      header: {
        "content-type": "multipart/form-data"
      }
    };

    await axios
      .post("http://3.35.19.190/diary/img", formData, config)
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  const InputProps = {
    ...getInputProps(),
    multiple: false,
    accept: "image/gif, image/jpg, image/jpeg"
  };

  return (
    <div>
      <div {...getRootProps()} maxsize={100} multiple={false}>
        <input {...InputProps} />
        {isDragActive ? (
          <div>파일을 여기 업로드하세요</div>
        ) : (
          <div>
            <button>업로드</button>
          </div>
        )}
      </div>
      <Link to="./Result">
        <button>제출</button>
      </Link>
    </div>
  );
}
