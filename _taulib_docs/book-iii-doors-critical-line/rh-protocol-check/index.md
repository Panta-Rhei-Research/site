---
{
  "projection_kind": "taulib_declaration",
  "title": "rh_protocol_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/rh-protocol-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::rh_protocol_check",
  "declaration_slug": "rh-protocol-check",
  "kind": "def",
  "name": "rh_protocol_check",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 130,
  "source_line_end": 149,
  "registry_ids": [
    "III.P11"
  ],
  "related_registry_items": [
    {
      "id": "III.P11",
      "title": "Primorial RH Verification Protocol",
      "url": "/registry/object/III.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L130-L149",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.CriticalLine",
        "url": "/verify/taulib/docs/book-iii-doors-critical-line/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L130-L149",
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

- Module: [TauLib.BookIII.Doors.CriticalLine](/verify/taulib/docs/book-iii-doors-critical-line/)
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L130-L149)
- Source range: L130-L149
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P11` — Primorial RH Verification Protocol

## Immediate Comment / Docstring

```lean
/-- [III.P11] Primorial RH verification protocol at depth k.
    Six steps: (i) compute Spec(H_{≤k}), (ii) verify eigenvalues real,
    (iii) verify zero locations, (iv) tower coherence, (v) CRT consistency,
    (vi) record certificate. Returns true if all steps pass. -/
```

## Source Excerpt

```lean
def rh_protocol_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- (i) Compute spectrum: eigenvalues 0², 1², ..., k²
      let spec_ok := kirchhoff_check k
      -- (ii) Verify eigenvalues real: all are Nat (always true)
      let real_ok := self_adjoint_check k
      -- (iii) Verify zero structure: spectral correspondence
      let zero_ok := spectral_correspondence_finite k
      -- (iv) Tower coherence: eigenvalue nesting at this depth
      let tower_ok := eigenvalue_nesting_check k
      -- (v) CRT consistency: Euler product at this level
      let crt_ok := bipolar_euler_check k
      -- (vi) Certificate: all checks pass (this function is the certificate)
      spec_ok && real_ok && zero_ok && tower_ok && crt_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
