import  {useState, useEffect} from 'react';
import postsData from '../data/data.json'
import PostList from './PostList'
import './card.css'

// Define the type for a single post
interface Post {
    id: number;
    title: string;
    content: string;
    author: string;
  }



// Function to shuffle an array of posts
const shuffleArray = (array: Post[]): Post[] => {
    return array.sort(() => Math.random() - 0.5);
  };

const Card = () => {
    const [randomPosts, setRandomPosts] = useState<Post[]>([]); // Define state type as an array of Post objects

    useEffect(()=>{
        //shufffle the posts
        const shuffledPosts = shuffleArray(postsData).slice(0,6);
        setRandomPosts(shuffledPosts)
    }, [])

  return (
    <div className='main'>
      <h1>Posts</h1>
       <div className="post-list">
        {randomPosts && randomPosts.map((post) => (
            <PostList key={post.id} post={post}/>
        ))}
       </div>
    </div>
  )
}

export default Card