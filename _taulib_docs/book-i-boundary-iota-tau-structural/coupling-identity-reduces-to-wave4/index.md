---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_identity_reduces_to_wave4",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/coupling-identity-reduces-to-wave4/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::coupling_identity_reduces_to_wave4",
  "declaration_slug": "coupling-identity-reduces-to-wave4",
  "kind": "theorem",
  "name": "coupling_identity_reduces_to_wave4",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 195,
  "source_line_end": 205,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L195-L205",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.IotaTauStructural",
        "url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L195-L205",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.IotaTauStructural](/verify/taulib/docs/book-i-boundary-iota-tau-structural/)
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L195-L205)
- Source range: L195-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Coupling-identity link (structural side)**: the Wave 4 capstone
    `iota_tau · (π + e) ≡ 2` transfers to *any* crossing-point defect
    germ *modulo* the Cauchy-equivalence-respects-multiplication
    bridge.  Packaged here as the reduction we need, not the analytic
    closure (which is a separable Wave 2-style infrastructure piece —
    "multiplication by a Cauchy sequence respects Cauchy equivalence" —
    recorded as a future deliverable).

    Concretely: given `Read g ≡ TauReal.iota_tau`, the conclusion
    `Read g · (π + e) ≡ 2` follows once we supply
    `mul_respects_equiv_left`, which states that multiplication by a
    fixed TauReal preserves Cauchy equivalence on the other factor.
    That theorem is the target of a dedicated future sub-wave that
    sits in `Boundary/TauRealMulCongr.lean` (Wave 2.5-style). -/
```

## Source Excerpt

```lean
theorem coupling_identity_reduces_to_wave4
    (g : CrossingPointDefectGerm) (h : IsCrossingPoint g)
    (mul_respects_equiv_left :
      ∀ (a b c : TauReal), TauReal.equiv a b →
        TauReal.equiv (a.mul c) (b.mul c)) :
    TauReal.equiv ((Read g).mul (TauReal.pi.add TauReal.e)) TauReal.two := by
  have h_read := iota_tau_read_eq_division g h
  have h_mul_equiv :=
    mul_respects_equiv_left (Read g) TauReal.iota_tau
      (TauReal.pi.add TauReal.e) h_read
  exact TauReal.equiv_trans h_mul_equiv TauReal.iota_tau_mul_pi_plus_e_eq_two
```
