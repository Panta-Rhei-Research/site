---
{
  "projection_kind": "taulib_declaration",
  "title": "code_spectral_scan_residues",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-spectral-scan-residues/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_spectral_scan_residues",
  "declaration_slug": "code-spectral-scan-residues",
  "kind": "def",
  "name": "code_spectral_scan_residues",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 256,
  "source_line_end": 269,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L256-L269",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.CodeDecode",
        "url": "/verify/taulib/docs/book-ii-regularity-code-decode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L256-L269",
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

- Module: [TauLib.BookII.Regularity.CodeDecode](/verify/taulib/docs/book-ii-regularity-code-decode/)
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L256-L269)
- Source range: L256-L269
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: scan residue classes for a given prime to find differing coefficients. -/
```

## Source Excerpt

```lean
def code_spectral_scan_residues (f g : TauIdx → Int)
    (k pi_idx : TauIdx) : Bool :=
  let p := nth_prime pi_idx
  go f g k pi_idx p 0 (p + 1)
where
  go (f g : TauIdx → Int) (k pi_idx p v fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if v >= p then false
    else
      let cf := code_spectral f k pi_idx v
      let cg := code_spectral g k pi_idx v
      if cf != cg then true
      else go f g k pi_idx p (v + 1) (fuel - 1)
  termination_by fuel
```
