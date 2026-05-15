---
{
  "projection_kind": "taulib_declaration",
  "title": "H0_tension_structural",
  "permalink": "/corpus/taulib/docs/book-v-temporal-distance-ladder/h0-tension-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::H0_tension_structural",
  "declaration_slug": "h0-tension-structural",
  "kind": "theorem",
  "name": "H0_tension_structural",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/corpus/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 228,
  "source_line_end": 230,
  "registry_ids": [
    "V.T18"
  ],
  "related_registry_items": [
    {
      "id": "V.T18",
      "title": "Hubble Tension Resolution",
      "url": "/registry/object/V.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L228-L230",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/corpus/taulib/docs/book-v-temporal-distance-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L228-L230",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/corpus/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L228-L230)
- Source range: L228-L230
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.T18` — Hubble Tension Resolution

## Immediate Comment / Docstring

```lean
/-- [V.T18] Hubble tension is structural: "early" (CMB) and "late" (Cepheid)
    rungs probe different orbit-depth regimes. If the readout functor R_d
    is nonlinear, they yield different H₀ values.

    Structural fact: CMB and Cepheid operate at different scales. -/
```

## Source Excerpt

```lean
theorem H0_tension_structural :
    DistanceLadderRung.CMB.log10_parsec ≠ DistanceLadderRung.Cepheid.log10_parsec := by
  simp [DistanceLadderRung.log10_parsec]
```
