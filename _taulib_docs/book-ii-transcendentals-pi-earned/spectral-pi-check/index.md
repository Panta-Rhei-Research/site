---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_pi_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/spectral-pi-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.PiEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.PiEarned::spectral_pi_check",
  "declaration_slug": "spectral-pi-check",
  "kind": "def",
  "name": "spectral_pi_check",
  "module_name": "TauLib.BookII.Transcendentals.PiEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/",
  "source_line_start": 107,
  "source_line_end": 111,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L107-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.PiEarned",
        "url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L107-L111",
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

- Module: [TauLib.BookII.Transcendentals.PiEarned](/verify/taulib/docs/book-ii-transcendentals-pi-earned/)
- Source path: [`TauLib/BookII/Transcendentals/PiEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L107-L111)
- Source range: L107-L111
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T22, perspective 2] Spectral evidence: the number of
    B-residues mod p_k (complete residue system) witnesses the
    winding number. At prime p_k, B cycles through p_k values,
    contributing 2*pi/p_k angular width per residue.

    The full circle 2*pi is partitioned into p_k arcs.
    Evidence: residue count = p_k exactly. -/
```

## Source Excerpt

```lean
def spectral_pi_check (bound : TauIdx) : Bool :=
  -- At k=1: p_1=2, so 2 B-residues -> half-circle = pi
  -- At k=2: p_2=3, so 3 B-residues -> third-circle = 2*pi/3
  circle_profinite_b_check 1 bound &&
  circle_profinite_b_check 2 bound
```
