import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();

    // In a real application, you would:
    // 1. Validate the data
    // 2. Send an email notification
    // 3. Save the submission to a database

    console.log('New Contact Form Submission:', body);

    return NextResponse.json({ message: 'Submission successful!' }, { status: 200 });
  } catch (error) {
    console.error('Error processing contact form:', error);
    return NextResponse.json({ message: 'Error processing request' }, { status: 500 });
  }
}
