---
{
  "projection_kind": "taulib_declaration",
  "title": "code_spectral_separation_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-spectral-separation-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_spectral_separation_check",
  "declaration_slug": "code-spectral-separation-check",
  "kind": "def",
  "name": "code_spectral_separation_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 291,
  "source_line_end": 302,
  "registry_ids": [
    "II.T35"
  ],
  "related_registry_items": [
    {
      "id": "II.T35",
      "title": "Code/Decode Bijection",
      "url": "/registry/object/II.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L291-L302",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L291-L302",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L291-L302)
- Source range: L291-L302
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Spectral completeness: the per-prime projections determine f.
    For distinct functions f, g on Z/P_kZ, there exists a prime p and
    residue v such that code_spectral(f, k, p, v) != code_spectral(g, k, p, v).

    Verified: for f = delta_0 and g = delta_1, the spectral coefficients differ. -/
```

## Source Excerpt

```lean
def code_spectral_separation_check (k_max : TauIdx) : Bool :=
  go 1 (k_max + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let delta_0 : TauIdx → Int := fun x => if x == 0 then 1 else 0
      let delta_1 : TauIdx → Int := fun x => if x == 1 then 1 else 0
      let ok := code_spectral_find_separator delta_0 delta_1 k
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
