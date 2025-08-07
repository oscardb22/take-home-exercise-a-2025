import React, {useState, useEffect} from 'react'

const ImageUrlChecker = (props) => {
    const [urlInput, setUrlInput] = useState("")
    const [isImage, setIsImage] = useState(false)
    const [isFile, setIsFile] = useState(false)

    // A basic regex for common image file extensions
    const imageRegex = /\.(jpeg|jpg|gif|png|bmp|webp|svg)$/i
    const fileRegex = /\.(csv|pdf|txt|doc|docx|xml|xmlx)$/i
    const value = props.urlImage || ""
    const errorImage = (e) => {
        e.target.onerror = null
        e.target.alt = "Error"
        e.target.src = "./src/assets/images/file_broken.svg"
    }

    useEffect(() => {
        setUrlInput(value)
        if (typeof value === "string") {
            try {
                new URL(value)
                if (imageRegex.test(value)) {
                    setIsImage(true)
                    setIsFile(false)
                }else if (fileRegex.test(value)){
                    setIsImage(false)
                    setIsFile(true)
                    setUrlInput("./src/assets/images/file_blue.svg")
                } else {
                    setIsImage(false)
                    setIsFile(false)
                }
            } catch (error) {
                setIsImage(false)
                setIsFile(false)
            }
        }
        return () => {}
    }, [value, imageRegex, fileRegex])

  return (
    <>
    {isImage || isFile ? (
          <img
            src={urlInput}
            alt="Preview"
            style={{ maxWidth: '50%', maxHeight: '200px', }}
            onError={errorImage}
          />
      ): value}
    </>
  )
}

export default ImageUrlChecker
