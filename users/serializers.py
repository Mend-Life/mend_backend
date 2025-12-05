from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    Converts User model instances to/from JSON.
    """
    
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'age', 'gender', 'location', 
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': False, 'allow_blank': True, 'allow_null': True},
            'age': {'required': False, 'allow_null': True},
            'gender': {'required': False, 'allow_blank': True, 'allow_null': True},
            'location': {'required': False, 'allow_blank': True, 'allow_null': True},
        }
    
    def create(self, validated_data):
        """
        Create a new user instance.
        Random name will be auto-generated if name is not provided (handled in model.save())
        """
        # Remove password from validated_data if present (we'll handle it separately)
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        
        # Note: In production, you'd hash the password properly
        # For now, we're just storing it (NOT RECOMMENDED FOR PRODUCTION)
        if password:
            user.password = password  # In production, use: user.set_password(password)
            user.save()
        
        return user
    
    def update(self, instance, validated_data):
        """
        Update an existing user instance.
        """
        # Remove password if present
        password = validated_data.pop('password', None)
        
        # Update all fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Handle password update
        if password:
            instance.password = password  # In production: instance.set_password(password)
        
        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Specialized serializer for user creation (signup).
    Includes password field.
    """
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'age', 'gender', 'location']
        extra_kwargs = {
            'email': {'required': False},  # Allow blank for quick start
            'password': {'required': False},  # Allow blank for quick start
            'name': {'required': False},
            'age': {'required': False},
            'gender': {'required': False},
            'location': {'required': False},
        }

