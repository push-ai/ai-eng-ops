"""
Well-structured database models for User Management System.

These models demonstrate proper field definitions, relationships, constraints,
indexes, and documentation for AI-friendly database design.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.utils import timezone


class User(models.Model):
    """
    User model representing a user in the system.
    
    This model stores user information including contact details and metadata.
    All users must have a unique email address which serves as the primary identifier.
    
    Attributes:
        email: Unique email address (required, indexed, unique)
        name: User's full name (required, max 100 characters)
        age: User's age (required, 0-150 range)
        created_at: Timestamp when user was created (auto-set)
        updated_at: Timestamp when user was last updated (auto-updated)
    
    Relationships:
        posts: Related posts authored by this user (reverse ForeignKey)
        comments: Related comments authored by this user (reverse ForeignKey)
    
    Example:
        >>> user = User.objects.create(
        ...     email='alice@example.com',
        ...     name='Alice Smith',
        ...     age=25
        ... )
        >>> user.is_adult()
        True
    """
    
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        null=False,
        blank=False,
        help_text="User's unique email address (primary identifier)",
        validators=[EmailValidator()]
    )
    
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        help_text="User's full name (1-100 characters)"
    )
    
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0, message="Age must be at least 0"),
            MaxValueValidator(150, message="Age must be at most 150")
        ],
        help_text="User's age (0-150)"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="Timestamp when user was created"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when user was last updated"
    )
    
    class Meta:
        """Model metadata."""
        db_table = 'users'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
        ]
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self) -> str:
        """String representation of the user."""
        return f"{self.name} ({self.email})"
    
    def __repr__(self) -> str:
        """Developer representation of the user."""
        return f"<User id={self.id} email={self.email}>"
    
    @property
    def is_adult(self) -> bool:
        """
        Check if user is an adult (age >= 18).
        
        Returns:
            bool: True if user is 18 or older, False otherwise
        """
        return self.age >= 18
    
    @property
    def post_count(self) -> int:
        """
        Get the number of posts authored by this user.
        
        Returns:
            int: Number of posts
        """
        return self.posts.count()
    
    @property
    def comment_count(self) -> int:
        """
        Get the number of comments authored by this user.
        
        Returns:
            int: Number of comments
        """
        return self.comments.count()
    
    def clean(self):
        """Validate model data before saving."""
        if self.age < 0 or self.age > 150:
            raise models.ValidationError({
                'age': 'Age must be between 0 and 150'
            })
        super().clean()
    
    def save(self, *args, **kwargs):
        """Override save to ensure clean() is called."""
        self.full_clean()
        super().save(*args, **kwargs)


class Post(models.Model):
    """
    Post model representing a blog post or article.
    
    Posts are authored by users and can have multiple comments.
    Posts have a title, content, and timestamps.
    
    Attributes:
        title: Post title (required, max 200 characters, indexed)
        content: Post content/body (required)
        author: ForeignKey to User (required, CASCADE on delete)
        created_at: Timestamp when post was created (auto-set, indexed)
        updated_at: Timestamp when post was last updated (auto-updated)
    
    Relationships:
        author: User who created this post (ForeignKey)
        comments: Comments on this post (reverse ForeignKey)
    
    Example:
        >>> user = User.objects.get(email='alice@example.com')
        >>> post = Post.objects.create(
        ...     title='My First Post',
        ...     content='This is the content...',
        ...     author=user
        ... )
        >>> post.word_count
        4
    """
    
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        db_index=True,
        help_text="Post title (1-200 characters)"
    )
    
    content = models.TextField(
        null=False,
        blank=False,
        help_text="Post content/body"
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        null=False,
        blank=False,
        db_index=True,
        help_text="User who created this post"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="Timestamp when post was created"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when post was last updated"
    )
    
    class Meta:
        """Model metadata."""
        db_table = 'posts'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author', 'created_at']),
            models.Index(fields=['created_at']),
        ]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        """String representation of the post."""
        return f"{self.title} by {self.author.name}"
    
    def __repr__(self) -> str:
        """Developer representation of the post."""
        return f"<Post id={self.id} title={self.title[:30]}>"
    
    @property
    def word_count(self) -> int:
        """
        Get the number of words in the post content.
        
        Returns:
            int: Number of words
        """
        return len(self.content.split())
    
    @property
    def comment_count(self) -> int:
        """
        Get the number of comments on this post.
        
        Returns:
            int: Number of comments
        """
        return self.comments.count()
    
    def clean(self):
        """Validate model data before saving."""
        if not self.title or len(self.title.strip()) == 0:
            raise models.ValidationError({
                'title': 'Title cannot be empty'
            })
        if not self.content or len(self.content.strip()) == 0:
            raise models.ValidationError({
                'content': 'Content cannot be empty'
            })
        super().clean()
    
    def save(self, *args, **kwargs):
        """Override save to ensure clean() is called."""
        self.full_clean()
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Comment model representing a comment on a post.
    
    Comments are authored by users and belong to a specific post.
    Comments have content and timestamps.
    
    Attributes:
        post: ForeignKey to Post (required, CASCADE on delete)
        author: ForeignKey to User (required, CASCADE on delete)
        content: Comment content/body (required)
        created_at: Timestamp when comment was created (auto-set, indexed)
        updated_at: Timestamp when comment was last updated (auto-updated)
    
    Relationships:
        post: Post this comment belongs to (ForeignKey)
        author: User who created this comment (ForeignKey)
    
    Example:
        >>> post = Post.objects.get(title='My First Post')
        >>> user = User.objects.get(email='bob@example.com')
        >>> comment = Comment.objects.create(
        ...     post=post,
        ...     author=user,
        ...     content='Great post!'
        ... )
    """
    
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        blank=False,
        db_index=True,
        help_text="Post this comment belongs to"
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        blank=False,
        db_index=True,
        help_text="User who created this comment"
    )
    
    content = models.TextField(
        null=False,
        blank=False,
        help_text="Comment content/body"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="Timestamp when comment was created"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when comment was last updated"
    )
    
    class Meta:
        """Model metadata."""
        db_table = 'comments'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['post', 'created_at']),
            models.Index(fields=['author', 'created_at']),
            models.Index(fields=['created_at']),
        ]
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self) -> str:
        """String representation of the comment."""
        return f"Comment by {self.author.name} on {self.post.title}"
    
    def __repr__(self) -> str:
        """Developer representation of the comment."""
        return f"<Comment id={self.id} post_id={self.post_id}>"
    
    @property
    def word_count(self) -> int:
        """
        Get the number of words in the comment content.
        
        Returns:
            int: Number of words
        """
        return len(self.content.split())
    
    def clean(self):
        """Validate model data before saving."""
        if not self.content or len(self.content.strip()) == 0:
            raise models.ValidationError({
                'content': 'Content cannot be empty'
            })
        super().clean()
    
    def save(self, *args, **kwargs):
        """Override save to ensure clean() is called."""
        self.full_clean()
        super().save(*args, **kwargs)

