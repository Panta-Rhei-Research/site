---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_identity",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/coupling-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::coupling_identity",
  "declaration_slug": "coupling-identity",
  "kind": "theorem",
  "name": "coupling_identity",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 246,
  "source_line_end": 252,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L246-L252",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L246-L252",
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
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L246-L252)
- Source range: L246-L252
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Coupling identity, fully zero-arg form** — the capstone
    closing the Wave 2.5 / H3 Wave 7 ledger-book.

    Uses the concrete `(π + e)`-bound `pi_plus_e_abs_le_seven` from
    `TauRealPiPlusE.lean` (established via Wave 3 monotonicity
    infrastructure: `pi_partial_le_19_div_6` + `e_partial_le_three`,
    each via telescoping on `sumFromTo_{pi_pair_term,e_term}_bound`)
    to automate the `M = 7`, `1 ≤ M`, and `∀ n, |(π+e).approx n| ≤ M`
    parameters, leaving only the germ and the crossing-point
    hypothesis.

    This retires the last Wave 2.5 / Wave 7 loose end: the
    structural coupling identity `Read(Δ_ω) · (π + e) ≡ 2` now holds
    at Cauchy equivalence for every crossing-point defect germ,
    without any explicit bound-parameter plumbing.  Combined with
    the Wave 4 numerical capstone `iota_tau_mul_pi_plus_e_eq_two`,
    this closes the H3 structural arc at full generality. -/
```

## Source Excerpt

```lean
theorem coupling_identity
    (g : CrossingPointDefectGerm) (h : IsCrossingPoint g) :
    TauReal.equiv ((Read g).mul (TauReal.pi.add TauReal.e)) TauReal.two :=
  coupling_identity_via_bounded_mul g h 7 (by norm_num)
    TauReal.pi_plus_e_abs_le_seven

end Tau.Boundary
```
