---
{
  "projection_kind": "taulib_declaration",
  "title": "brun_euler_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-euler-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::brun_euler_check",
  "declaration_slug": "brun-euler-check",
  "kind": "def",
  "name": "brun_euler_check",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 228,
  "source_line_end": 239,
  "registry_ids": [
    "III.T67"
  ],
  "related_registry_items": [
    {
      "id": "III.T67",
      "title": "Sieve-Tower Compatibility",
      "url": "/registry/object/III.T67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L228-L239",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.SieveInfrastructure",
        "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L228-L239",
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

- Module: [TauLib.BookIII.Spectral.SieveInfrastructure](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/)
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L228-L239)
- Source range: L228-L239
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T67` — Sieve-Tower Compatibility

## Immediate Comment / Docstring

```lean
/-- [III.T67] Brun sieve matches Euler phi at primorial levels. -/
```

## Source Excerpt

```lean
def brun_euler_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      let brun := brun_sieve_count pk k
      let phi := euler_phi_primorial k
      (brun == phi) && go (k + 1) (fuel - 1)
  termination_by fuel
```
