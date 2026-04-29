---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_correspondence_O3",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/spectral-correspondence-o3/",
  "summary_short": "`axiom` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_correspondence_O3",
  "declaration_slug": "spectral-correspondence-o3",
  "kind": "axiom",
  "name": "spectral_correspondence_O3",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 126,
  "source_line_end": 127,
  "registry_ids": [
    "III.T18"
  ],
  "related_registry_items": [
    {
      "id": "III.T18",
      "title": "Spectral Correspondence Theorem",
      "url": "/registry/object/III.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L126-L127",
  "formal_status": "axiom",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralCorrespondence",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L126-L127",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "axiom",
      "status": "axiom"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Doors.SpectralCorrespondence](/verify/taulib/docs/book-iii-doors-spectral-correspondence/)
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L126-L127)
- Source range: L126-L127
- Kind: `axiom`
- Formal status hint: `axiom`

## Registry Links

- `III.T18` — Spectral Correspondence Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T18] **CONJECTURE-AXIOM — CONDITIONAL RESULTS DOWNSTREAM**

    The O(3) spectral correspondence holds at all levels. This is one
    of exactly three conjecture-axioms in TauLib; see also
    `bridge_functor_exists` (`BookIII.Bridge.BridgeAxiom`) and
    `grand_grh_adelic` (`BookIII.Doors.GrandGRH`).

    **Conjectural scope.** At each finite level `k`,
    `spectral_correspondence_finite k` is decidable and verified
    computationally via `native_decide`. The axiom asserts that the
    finite correspondence extends to the universal statement
    `∀ k : Nat`. That extension is the conjectural content.

    **Mathematical content.**  The spectral correspondence claims
    `ζ_τ(s) = 0 ⟺ Λ(s) ∈ Spec(H_L)`, with the determinant
    representation `ζ_τ(s) = det(I − Λ(s)·H_L⁻¹)`. This is the
    framework's honest conjectural gap in the τ-approach to RH.

    **Downstream theorems are CONDITIONAL RESULTS.** Any theorem
    whose transitive proof chain invokes
    `spectral_correspondence_O3` is conditional on the universal
    extension. Running `#print axioms <theorem-name>` on a
    downstream theorem will list `spectral_correspondence_O3`;
    readers should treat that theorem as a conditional result.

    **Preferred encoding (future work).** As with
    `bridge_functor_exists`, the Mathlib-community idiom would
    refactor downstream theorems to take this conjecture as an
    explicit hypothesis. Planned for a future wave. -/
```

## Source Excerpt

```lean
axiom spectral_correspondence_O3 :
  ∀ k : Nat, spectral_correspondence_finite k = true
```
