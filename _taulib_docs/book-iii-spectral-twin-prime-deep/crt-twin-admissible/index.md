---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_twin_admissible",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/crt-twin-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::crt_twin_admissible",
  "declaration_slug": "crt-twin-admissible",
  "kind": "def",
  "name": "crt_twin_admissible",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 120,
  "source_line_end": 130,
  "registry_ids": [
    "III.D107"
  ],
  "related_registry_items": [
    {
      "id": "III.D107",
      "title": "CRT Twin Admissibility",
      "url": "/registry/object/III.D107/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L120-L130",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L120-L130",
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

- Module: [TauLib.BookIII.Spectral.TwinPrimeDeep](/verify/taulib/docs/book-iii-spectral-twin-prime-deep/)
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L120-L130)
- Source range: L120-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D107` — CRT Twin Admissibility

## Immediate Comment / Docstring

```lean
/-- [III.D107] Count twin-admissible residues mod M_k. -/
```

## Source Excerpt

```lean
def crt_twin_admissible (k : Nat) : Nat :=
  let pk := primorial k
  go 0 0 (pk + 1)
where
  go (r acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if r >= primorial k then acc
    else
      let acc' := if is_twin_admissible r k then acc + 1 else acc
      go (r + 1) acc' (fuel - 1)
  termination_by fuel
```
