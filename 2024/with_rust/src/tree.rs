pub struct Tree<T> {
    val: T,
    left: Option<Box<Tree<T>>>,
    right: Option<Box<Tree<T>>>,
}

// impl Tree<T> {
//     fn fromIter(arr: Iterator<T>) -> Tree<T> {
//         Tree {
//             val: iter.next(),
//             left: Tree { val: iter.next() },
//             right: Tree { val: iter.next() },
//         }
//     }
// }
