
import './postlis.css'
//Define type
interface Post{
    id:number;
    title: string;
    content: string;
    author:string;
}

//define the props for PostList
interface PostListProps {
    post: Post;
}

const PostList: React.FC<PostListProps> = ({post}) => {
  

  return (
    <div className="card" key={post.id}>
        <h2>{post.title}</h2>
        <p>{post.content}</p>
        <p><strong>Author:</strong>{post.author}</p>
    </div>
  )
}

export default PostList