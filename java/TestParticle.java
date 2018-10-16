class TestParticle{
    public static void main(String[] args) {
        Particle[] gravel = new Particle[4];
        gravel[0] = new Particle(0.1, new double[] {0.5, 0.2, 0.0});
        gravel[1] = new Particle(0.3, new double[] {0.7, 0.4, 0.0});
        gravel[2] = new Particle(0.2, new double[] {0.2, 0.7, 0.0});
        gravel[3] = new Particle(0.05, new double[] {0.3, 0.1, 0.0});
        
    }
}