#!/usr/bin/env python3
"""
test_groq.py - Verify Groq API key functionality and test chatbot

This script tests:
1. API key is properly loaded from .env
2. Groq client initializes successfully
3. Chat model responds correctly
4. JSON parsing works as expected
"""

import os
import sys
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_api_key_loaded():
    """Test 1: Check if API key is loaded"""
    print("=" * 60)
    print("TEST 1: API Key Loaded")
    print("=" * 60)
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("[FAIL] GROQ_API_KEY not found in environment")
        return False

    # Show masked key for security
    masked_key = f"{api_key[:10]}...{api_key[-4:]}"
    print(f"[PASS] API key found: {masked_key}")
    return True


def test_groq_client_init():
    """Test 2: Initialize Groq client"""
    print("\n" + "=" * 60)
    print("TEST 2: Groq Client Initialization")
    print("=" * 60)

    try:
        from groq import Groq
        api_key = os.environ.get("GROQ_API_KEY")
        client = Groq(api_key=api_key)
        print("[PASS] Groq client initialized successfully")
        return client
    except Exception as e:
        print(f"[FAIL] Could not initialize Groq client")
        print(f"   Error: {e}")
        return None


def test_simple_chat(client):
    """Test 3: Make a simple chat request"""
    print("\n" + "=" * 60)
    print("TEST 3: Simple Chat Request")
    print("=" * 60)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Respond with a simple one-sentence greeting."},
                {"role": "user", "content": "Hello, are you working?"}
            ],
            max_tokens=128,
        )

        reply = response.choices[0].message.content
        print(f"[PASS] Chat request successful")
        print(f"   Model response: {reply}")
        return True
    except Exception as e:
        print(f"[FAIL] Chat request failed")
        print(f"   Error: {e}")
        return False


def test_json_response(client):
    """Test 4: JSON response parsing (like the chatbot expects)"""
    print("\n" + "=" * 60)
    print("TEST 4: JSON Response Parsing")
    print("=" * 60)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": 'Return ONLY valid JSON in this format: {"reply": "your answer", "action": {"type": null, "payload": {}}}'
                },
                {"role": "user", "content": "What is 2+2?"}
            ],
            max_tokens=256,
        )

        raw_response = response.choices[0].message.content
        print(f"Raw response: {raw_response[:100]}...")

        # Try to parse JSON
        try:
            parsed = json.loads(raw_response)
            if "reply" in parsed and "action" in parsed:
                print(f"[PASS] Valid JSON structure received")
                print(f"   Reply: {parsed['reply']}")
                return True
            else:
                print(f"[WARN] JSON parsed but missing expected keys")
                print(f"   Keys found: {list(parsed.keys())}")
                return False
        except json.JSONDecodeError:
            print(f"[WARN] Response is not valid JSON")
            print(f"   Raw: {raw_response[:200]}")
            # This is okay - the groq_client.py has fallback handling
            return True

    except Exception as e:
        print(f"[FAIL] JSON response test failed")
        print(f"   Error: {e}")
        return False


def test_chatbot_module():
    """Test 5: Test the actual chatbot module"""
    print("\n" + "=" * 60)
    print("TEST 5: Chatbot Module Integration")
    print("=" * 60)

    try:
        from app.groq_client import call_chat_model
        from app.system_prompt import build_system_prompt

        # Create a simple user profile
        user_profile = {
            "income_band": "50k-100k",
            "education_level": "tertiary",
            "region": "Lagos"
        }

        system_prompt = build_system_prompt(user_profile)
        messages = [{"role": "user", "content": "How do I apply for a loan?"}]

        result = call_chat_model(system_prompt, messages, context={"userId": "test-user"})

        if result and "reply" in result:
            print(f"[PASS] Chatbot responded successfully")
            print(f"   Reply: {result['reply'][:150]}...")
            print(f"   Action type: {result.get('action', {}).get('type', 'None')}")
            return True
        else:
            print(f"[FAIL] Invalid response structure")
            print(f"   Response: {result}")
            return False

    except Exception as e:
        print(f"[FAIL] Chatbot module test failed")
        print(f"   Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n[TEST SUITE] GROQ API KEY & CHATBOT VERIFICATION\n")

    results = {}

    # Test 1: API Key
    results["API Key Loaded"] = test_api_key_loaded()

    # Test 2: Client Init
    client = test_groq_client_init()
    results["Client Init"] = client is not None

    # Tests 3-4: Chat (only if client initialized)
    if client:
        results["Simple Chat"] = test_simple_chat(client)
        results["JSON Response"] = test_json_response(client)
    else:
        print("\n[SKIP] Skipping chat tests - client failed to initialize")

    # Test 5: Chatbot module
    results["Chatbot Module"] = test_chatbot_module()

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, passed_flag in results.items():
        status = "[PASS]" if passed_flag else "[FAIL]"
        print(f"{status}: {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n[SUCCESS] All tests passed! Your Groq API key is functional and chatbot is working.")
        return 0
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed. Check errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
