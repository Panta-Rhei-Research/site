---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_strict_witness_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/e2-strict-witness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::e2_strict_witness_check",
  "declaration_slug": "e2-strict-witness-check",
  "kind": "def",
  "name": "e2_strict_witness_check",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 180,
  "source_line_end": 199,
  "registry_ids": [
    "III.P34"
  ],
  "related_registry_items": [
    {
      "id": "III.P34",
      "title": "E₂ ⊋ E₁ Strict Witness",
      "url": "/registry/object/III.P34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L180-L199",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L180-L199",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L180-L199)
- Source range: L180-L199
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P34` — E₂ ⊋ E₁ Strict Witness

## Immediate Comment / Docstring

```lean
/-- [III.P34] E₂ strict witness: find an orbit with length > 2.
    E₁ orbits (bipolar involution) have length ≤ 2 (e₊↔e₋).
    E₂ orbits can have length 3, 5, etc. (prime orbit lengths). -/
```

## Source Excerpt

```lean
def e2_strict_witness_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- Find an orbit of length > 2
      let found := find_long_orbit 0 1 pk k pk
      found && go (k + 1) (fuel - 1)
  termination_by fuel
  find_long_orbit (c d pk k fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if d >= pk then false
    else
      let len := orbit_length c d k
      if len > 2 then true
      else find_long_orbit c (d + 1) pk k (fuel - 1)
  termination_by fuel
```
